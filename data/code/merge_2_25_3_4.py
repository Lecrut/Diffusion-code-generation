from abc import ABC, abstractmethod
class GeocodingProvider(ABC):
    @abstractmethod
    def get_name(self, lat: float, lon: float) -> str:
        pass
class OpenStreetMapProvider(GeocodingProvider):
    def __init__(self, api_key: str = "default_osm"):
        self.api_key = api_key
    def get_name(self, lat: float, lon: float) -> str:
        return f"OpenStreetMap Location ({lat}, {lon})"
class GoogleMapsProvider(GeocodingProvider):
    def __init__(self, api_key: str = "default_google"):
        self.api_key = api_key
    def get_name(self, lat: float, lon: float) -> str:
        return f"Google Maps Location ({lat}, {lon})"
class GeographicMapper:
    def __init__(self):
        self.providers: list[GeocodingProvider] = []
    def add_provider(self, provider: GeocodingProvider) -> None:
        if isinstance(provider, GeocodingProvider):
            self.providers.append(provider)
        else:
            raise TypeError("Only valid geocoding providers can be added.")
    def map_coordinates_to_name(self, lat: float, lon: float, use_first_available: bool = True) -> str | None:
        for provider in self.providers:
            try:
                return provider.get_name(lat, lon)
            except Exception as e:
                if not use_first_available and len(self.providers) > 1:
                    continue
                raise e
    def map_coordinates_to_names(self, lat: float, lon: float) -> list[str]:
        results = []
        for provider in self.providers:
            try:
                name = provider.get_name(lat, lon)
                if name and len(name.strip()) > 0:
                    results.append(name)
            except Exception as e:
                pass
        return results
if __name__ == '__main__':
    mapper = GeographicMapper()
    osm_provider = OpenStreetMapProvider(api_key="osm_123")
    google_provider = GoogleMapsProvider(api_key="google_456")
    mapper.add_provider(osm_provider)
    mapper.add_provider(google_provider)
    lat, lon = 40.7128, -74.0060
    single_name = mapper.map_coordinates_to_name(lat, lon)
    all_names = mapper.map_coordinates_to_names(lat, lon)
    print(f"Single Name: {single_name}")
    print("All Names:")
    for name in all_names:
        print(name)