from typing import List, Optional

# from geojson_pydantic import Feature, Geometry
from geojson_pydantic.features import Feature, FeatureCollection, Geometry

# from geojson_pydantic.geometries import Geometry
from pydantic import BaseModel


# Shared properties
class BibAreasTypesBase(BaseModel):
    type_name: Optional[str] = None
    type_code: str
    type_desc: Optional[str] = None
    ref_name: Optional[str] = None
    ref_version: Optional[str] = None
    num_version: Optional[str] = None


class BibAreasTypesInDBase(BibAreasTypesBase):
    id_type: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class BibAreasTypes(BibAreasTypesInDBase):
    pass


# Additional properties stored in DB
class BibAreasTypesInDB(BibAreasTypesInDBase):
    pass


class LAreasBase(BaseModel):
    area_name: str
    area_code: str
    # geom: Geometry
    source: Optional[str] = None
    area_type: BibAreasTypes


class LAreasBaseInDBase(LAreasBase):
    id_area: int
    id_type: int

    class Config:
        orm_mode = True


class LAreas(LAreasBaseInDBase):
    pass


class LAreasGeoJson(Feature):
    properties: LAreasBase
    type: str = "multipolygon"


class LAreasGeoJsonList(FeatureCollection):
    features: List[LAreasGeoJson]
