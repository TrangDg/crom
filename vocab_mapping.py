
import inspect
from cidoc_orm import Identifier, Mark, ManMadeObject, Type, \
	Person, Material, MeasurementUnit, Place, Dimension, \
	ConceptualObject, TimeSpan, Actor, PhysicalThing, \
	LinguisticObject, InformationObject, SpatialCoordinates, \
	Activity, Group, Appellation, MonetaryAmount, Purchase, \
	Destruction 

def register_aat_class(name, parent, id):
	c = type(name, (parent,), {})
	c._classification = "http://vocab.getty.edu/aat/%s" % id
	c._type = None # To avoid conflicting with parent class
	globals()[name] = c	

materialTypes = {}
def register_aat_material(name, id):
	m = Material("http://vocab.getty.edu/aat/%s" % id)
	m.label = name
	materialTypes[name] = m	

dimensionTypes = {}
def register_aat_dimensionType(name, id):
	d = Type("http://vocab.getty.edu/aat/%s" % id)
	d.label = name
	dimensionTypes[name] = d

dimensionUnits = {}
def register_aat_dimensionUnit(name, id):
	d = MeasurementUnit("http://vocab.getty.edu/aat/%s" % id)
	d.label = name
	dimensionUnits[name] = d

# Meta meta
ext_classes = {
	"LocalNumber": {"parent": Identifier, "vocab": "aat", "id": "300404621"},	
	"AccessionNumber": {"parent": Identifier, "vocab": "aat", "id": "300312355"},	
	"Inscription": {"parent": Mark, "vocab": "aat", "id": "300028702"},
	"Signature": {"parent": Mark, "vocab": "aat", "id": "300028705"},

	"MaterialStatement": {"parent": LinguisticObject, "vocab": "aat", "id": "300264237"},
	"DimensionStatement": {"parent": LinguisticObject, "vocab": "aat", "id": ""},
	"CreditStatement": {"parent": LinguisticObject, "vocab":"aat", "id": "300026687"},
	"CatalogueRaisonne": {"parent": InformationObject, "vocab":"aat", "id":"300026061"},
	"EditionStatement": {"parent": LinguisticObject, "vocab":"aat", "id":"300121294"},
	"BiographyStatement": {"parent": LinguisticObject, "vocab":"aat", "id":"300080102"},

	"Latitude": {"parent": SpatialCoordinates, "vocab":"aat", "id": "300387565"},
	"Longitude": {"parent": SpatialCoordinates, "vocab":"aat", "id": "300387567"},

	"Gallery": {"parent": Place, "vocab":"aat", "id": "300240057"},

	"Museum": {"parent": Group, "vocab": "aat", "id": "300312281"},
	"Department": {"parent": Group, "vocab":"aat", "id": "300263534"},
	"Nationality": {"parent": Group, "vocab":"aat", "id":"300379842"},

	"Auction": {"parent": Activity, "vocab": "aat", "id": "300054751"},

	"SupportPart": {"parent": PhysicalThing, "vocab":"aat", "id":"300014844"},
	"FramePart": {"parent": PhysicalThing, "vocab":"aat", "id":"300404391"},
	"MountPart": {"parent": PhysicalThing, "vocab":"aat", "id":"300131087"},
	"PanelPart": {"parent": PhysicalThing, "vocab":"aat", "id":"300014657"},

	"SortName": {"parent": Appellation, "vocab":"aat", "id":"300404672"},
	"DisplayName": {"parent": Appellation, "vocab":"aat", "id":"300404670"},
	"GivenName": {"parent": Appellation, "vocab":"aat", "id":"300404651"},
	"FamilyName": {"parent": Appellation, "vocab":"aat", "id":"300404652"},
	"MiddleName": {"parent": Appellation, "vocab":"aat", "id":"300404654"},
	"NamePrefix": {"parent": Appellation, "vocab":"aat", "id":"300404845"},
	"NameSuffix": {"parent": Appellation, "vocab":"aat", "id":"300404662"},

	"Painting": {"parent": ManMadeObject, "vocab": "aat", "id": "300033618"},
	"Sculpture": {"parent": ManMadeObject, "vocab": "aat", "id": "300047090"},
	"Drawing": {"parent": ManMadeObject, "vocab": "aat", "id": "300033973"},
	"Miniature": {"parent": ManMadeObject, "vocab": "aat", "id": "300033936"},
	"Tapestry": {"parent": ManMadeObject, "vocab": "aat", "id": "300205002"},
	"Furniture": {"parent": ManMadeObject, "vocab": "aat", "id": "300037680"},
	"Mosaic": {"parent": ManMadeObject, "vocab": "aat", "id": "300015342"},
	"Photograph": {"parent": ManMadeObject, "vocab": "aat", "id": "300046300"},
	"Drawing": {"parent": ManMadeObject, "vocab": "aat", "id": "300033973"},
	"Coin": {"parent": ManMadeObject, "vocab": "aat", "id": "300037222"},
	"Vessel": {"parent": ManMadeObject, "vocab": "aat", "id": "300193015"},
	"Graphic": {"parent": ManMadeObject, "vocab": "aat", "id": "300015387"},
	"Enamel": {"parent": ManMadeObject, "vocab": "aat", "id": "300178264"},
	"Embroidery": {"parent": ManMadeObject, "vocab": "aat", "id": "300264024"},
	"PhotographPrint": {"parent": ManMadeObject, "vocab": "aat", "id": "300127104"},
	"PhotographAlbum": {"parent": ManMadeObject, "vocab": "aat", "id": "300026695"},
	"PhotographBook": {"parent": ManMadeObject, "vocab": "aat", "id": "300265728"}
}
 
for (name,v) in ext_classes.items():
	register_aat_class(name, v['parent'], v['id'])


aat_material_mapping = {
	"panel": "300014657",  # Is really a support
	"watercolor": "300015045",
	"oil": "300015050",
	"tempera": "300015062",
	"canvas": "300014078",
	"oak": "300012264",
	"gold leaf": "300264831",
	"paper": "300014109",
	"copper": "300011020",
	"terracotta": "300010669",
	"glass": "300010797",
	"chalk": "300011727",
	"bronze": "300010957",
	"marble": "300011443",
	"albumen silver print": "300127121",
	"gelatin silver print": "300128695",
	"silver": "300011029"
}

# pen, pencil, card, cardboard, porcelain, wax, ceramic, plaster
# crayon, millboard, gouache, brass, stone, lead, iron, clay,
# alabaster, limestone

for (k,v) in aat_material_mapping.items():
	register_aat_material(k,v)

aat_culture_mapping = {
	"french": "300111188",
	"italian": "300111198",
	"german": "300111192",
	"dutch": "300020929"
}

dim_type_mapping = {
	"height": "300055644",
	"width": "300055647",
	"depth": "300072633",
	"diameter": "300055624",
	"weight": "300056240"
}

dim_unit_mapping = {
	"inches": "300379100",	
	"feet": "300379101",
	"cm": "300379098"
}
for (k,v) in dim_unit_mapping.items():
	register_aat_dimensionUnit(k,v)

# Monkey patch Type's _toJSON to only emit full data if not just URI+type
def typeToJSON(self, top=False):
	props = self.__dict__.keys()
	if len(props) > 3:
		return super(Type, self)._toJSON()
	else:
		# process id for known vocabs
		if self.id.startswith("http://vocab.getty.edu/aat/"):
			return self.id.replace("http://vocab.getty.edu/aat/", "aat:")
		return self.id
Type._toJSON = typeToJSON


# Stupid DestuctionActivity as CRM has a Destruction *event*
class DestructionActivity(Destruction, Activity):
	_uri_segment = "Activity"
	_type = ["crm:Destruction", "crm:Activity"]
	_niceType = ["Destruction", "Activity"]
DestructionActivity._classhier = inspect.getmro(DestructionActivity)[:-1]


# New Payment Activity
Purchase._properties['offering_price'] = {"rdf":"pi:had_offering_price", "range": MonetaryAmount}
class Payment(Activity):
	_properties = {
		"paid_amount": {"rdf": "pi:paid_amount", "range": MonetaryAmount},
		"paid_to": {"rdf": "pi:paid_to", "range": Actor},
		"paid_from": {"rdf": "pi:paid_from", "range": Actor}
	}
	_uri_segment = "Payment"
	_type = "pi:Payment"
Payment._classhier = inspect.getmro(Payment)[:-1]


# Add some further properties
Person._properties['familyName'] = {"rdf": "schema:familyName", "range": str}
Person._properties['givenName'] = {"rdf": "schema:givenName", "range": str}
Person._properties['nationality'] = {"rdf": "schema:nationality", "range": Place}
Person._properties['exactMatch'] = {"rdf": "skos:exactMatch", "range": Type}
Person._properties['closeMatch'] = {"rdf": "skos:closeMatch", "range": Type}

Place._properties['exactMatch'] = {"rdf": "skos:exactMatch", "range": Place}
Place._properties['closeMatch'] = {"rdf": "skos:closeMatch", "range": Place}

ManMadeObject._properties['culture'] = {"rdf": "schema:genre", "range": Type}
ManMadeObject._properties['height'] = {"rdf": "schema:height", "range": Dimension}
ManMadeObject._properties['width'] = {"rdf": "schema:width", "range": Dimension}
Material._properties['value'] = {"rdf": "rdf:value", "range": str}

endOfMonths = {'01': 31, '02': 28, '03':31, '04':30, '05':31, '06':30,\
	'07':31, '08':31, '09':30, '10':31, '11':30, '12':31}