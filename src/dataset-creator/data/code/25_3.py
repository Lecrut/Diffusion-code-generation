import abc
from typing import Optional
class GeocodingProvider(abc.ABC):
    @abc.abstractmethod
    def get_name(self, lat: float, lon: float) -> str:
        pass
class OpenStreetMapProvider(GeocodingProvider):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
    def get_name(self, lat: float, lon: float) -> str:
        return f"OpenStreetMap Location at ({lat}, {lon})"
class GoogleMapsProvider(GeocodingProvider):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
    def get_name(self, lat: float, lon: float) -> str:
        return f"Google Maps Location at ({lat}, {lon})"
class GeographicMapper:
    def __init__(self, provider: GeocodingProvider):
        self.provider = provider
    def map_coordinates_to_name(self, latitude: float, longitude: float) -> str:
        if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
            raise ValueError("Invalid coordinates")
        return self.provider.get_name(latitude, longitude)
if __name__ == '__main__':
    osm_provider = OpenStreetMapProvider()
    google_provider = GoogleMapsProvider(api_key="demo_key_12345")
    mapper_osm = GeographicMapper(osm_provider)
    mapper_google = GeographicMapper(google_provider)
    sample_lat, sample_lon = 40.7128, -74.0060
    result_osm = mapper_osm.map_coordinates_to_name(sample_lat, sample_lon)
    result_google = mapper_google.map_coordinates_to_name(sample_lat, sample_lon)
    print(f"OSM Result: {result_osm}")
    print(f"Google Maps Result: {result_google}")