import abc
from typing import Optional
class GeocodingProvider(abc.ABC):
    @abc.abstractmethod
    def get_name(self, latitude: float, longitude: float) -> str:
        pass
class GoogleMapsProvider(GeocodingProvider):
    def __init__(self, api_key: str = "YOUR_API_KEY"):
        self.api_key = api_key
    def get_name(self, latitude: float, longitude: float) -> str:
        return f"Google Maps Location ({latitude}, {longitude}) - Placeholder Data"
class OpenStreetMapProvider(GeocodingProvider):
    def __init__(self, user_agent: Optional[str] = None):
        self.user_agent = user_agent or "GeographicMapper/1.0"
    def get_name(self, latitude: float, longitude: float) -> str:
        return f"OpenStreetMap Location ({latitude}, {longitude}) - Placeholder Data"
class GeographicMapper:
    def __init__(self):
        self.providers = {}
    def register_provider(self, provider_class: type[GeocodingProvider], name: str):
        if not issubclass(provider_class, GeocodingProvider):
            raise TypeError("Only subclasses of GeocodingProvider are allowed")
        self.providers[name] = provider_class()
    def get_location_name(
        self, latitude: float, longitude: float, provider_name: Optional[str] = None
    ) -> str:
        if not provider_name and len(self.providers) == 1:
            for p in self.providers.values():
                return p.get_name(latitude, longitude)
        if provider_name not in self.providers:
            raise ValueError(f"Unknown provider '{provider_name}'. Available providers: {list(self.providers.keys())}")
        return self.providers[provider_name].get_name(latitude, longitude)
if __name__ == '__main__':
    mapper = GeographicMapper()
    google_provider = GoogleMapsProvider(api_key="test-key")
    osm_provider = OpenStreetMapProvider(user_agent=None)
    mapper.register_provider(GoogleMapsProvider, "google_maps")
    mapper.register_provider(OpenStreetMapProvider, "openstreetmap")
    lat, lon = 40.7128, -74.0060
    result_google = mapper.get_location_name(lat, lon, provider_name="google_maps")
    print(result_google)
    result_osm = mapper.get_location_name(lat, lon, provider_name="openstreetmap")
    print(result_osm)