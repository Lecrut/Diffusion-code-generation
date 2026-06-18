import abc
from typing import Optional
class GeocodingProvider(abc.ABC):
    @abc.abstractmethod
    def get_name(self, lat: float, lon: float) -> str:
        pass
class GoogleMapsProvider(GeocodingProvider):
    def __init__(self, api_key: str = "YOUR_API_KEY"):
        self.api_key = api_key
    def get_name(self, lat: float, lon: float) -> str:
        return f"Google Maps Location at {lat}, {lon}"
class OpenStreetMapProvider(GeocodingProvider):
    def __init__(self, user_agent: str = "PythonScript/1.0"):
        self.user_agent = user_agent
    def get_name(self, lat: float, lon: float) -> str:
        return f"OpenStreetMap Location at {lat}, {lon}"
class GeographicMapper:
    def __init__(self):
        self.providers: list[GeocodingProvider] = []
    def add_provider(self, provider: GeocodingProvider) -> None:
        if isinstance(provider, GeocodingProvider):
            self.providers.append(provider)
        else:
            raise TypeError("Only valid geocoding providers can be added.")
    def get_name_from_coordinates(
        self, lat: float, lon: float, provider_index: Optional[int] = None
    ) -> str:
        if not self.providers:
            return "No providers registered."
        if provider_index is not None and 0 <= provider_index < len(self.providers):
            selected_provider = self.providers[provider_index]
        else:
            if not self.providers:
                return "Error: No providers registered."
            selected_provider = self.providers[0]
        try:
            name = selected_provider.get_name(lat, lon)
            return f"Provider {selected_provider.__class__.__name__}: {name}"
        except Exception as e:
            return f"Error retrieving location from provider: {str(e)}"
if __name__ == '__main__':
    mapper = GeographicMapper()
    google_providers = GoogleMapsProvider(api_key="demo_key")
    osm_provider = OpenStreetMapProvider(user_agent="test_user")
    mapper.add_provider(google_providers)
    mapper.add_provider(osm_provider)
    lat, lon = 40.7128, -74.0060
    result_default = mapper.get_name_from_coordinates(lat, lon)
    print(result_default)
    result_specific = mapper.get_name_from_coordinates(lat, lon, provider_index=0)
    print(result_specific)