from abc import ABC, abstractmethod
class GeocodingProvider(ABC):
    @abstractmethod
    def get_name(self, latitude: float, longitude: float) -> str:
        pass
class MockGeocodingProvider(GeocodingProvider):
    _locations = {
        (40.7128, -74.0060): "New York City",
        (51.5074, -0.1278): "London",
        (35.6762, 139.6503): "Tokyo"
    }
    def get_name(self, latitude: float, longitude: float) -> str:
        key = (round(latitude, 4), round(longitude, 4))
        return self._locations.get(key, f"Unknown Location at {latitude}, {longitude}")
class GeographicMapper:
    def __init__(self):
        self.providers: list[GeocodingProvider] = []
    def add_provider(self, provider: GeocodingProvider) -> None:
        if isinstance(provider, GeocodingProvider):
            self.providers.append(provider)
        else:
            raise TypeError("Only instances of subclasses from 'abstract base pattern' are allowed")
    def get_name_for_coordinates(
        self, latitude: float | None = None, longitude: float | None = None
    ) -> str:
        if latitude is None or longitude is None:
            return "Invalid coordinates"
        for provider in self.providers:
            try:
                name = provider.get_name(latitude, longitude)
                return f"{name} (via {provider.__class__.__name__})"
            except Exception as e:
                continue
        return "No matching location found via any registered providers"
if __name__ == '__main__':
    mapper = GeographicMapper()
    mock_provider = MockGeocodingProvider()
    mapper.add_provider(mock_provider)
    test_lat, test_lon = 40.7128, -74.0060
    result = mapper.get_name_for_coordinates(test_lat, test_lon)
    print(result)