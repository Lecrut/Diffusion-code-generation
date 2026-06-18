from abc import ABC, abstractmethod
class GeocodingProvider(ABC):
    @abstractmethod
    def get_location(self, lat: float, lon: float) -> str:
        pass
class SampleLocationProvider(GeocodingProvider):
    _locations = {
        (40.7128, -74.0060): "New York",
        (51.5074, -0.1278): "London",
        (35.6762, 139.6503): "Tokyo"
    }
    def get_location(self, lat: float, lon: float) -> str:
        key = (lat, lon)
        return self._locations.get(key, f"Unknown location at {lat}, {lon}")
class SampleCityProvider(GeocodingProvider):
    _cities = [
        ("New York", 40.7128, -74.0060),
        ("London", 51.5074, -0.1278)
    ]
    def get_location(self, lat: float, lon: float) -> str:
        for city_name, c_lat, c_lon in self._cities:
            if abs(lat - c_lat) < 0.001 and abs(lon - c_lon) < 0.001:
                return city_name
        return f"Unknown location at {lat}, {lon}"
class GeographicMapper:
    def __init__(self, provider_class=None):
        self.provider = provider_class if isinstance(provider_class, GeocodingProvider) else SampleLocationProvider()
    def map_coordinates(self, lat: float, lon: float) -> str:
        return self.provider.get_location(lat, lon)
if __name__ == '__main__':
    mapper1 = GeographicMapper(SampleCityProvider())
    print(mapper1.map_coordinates(51.5074, -0.1278))
    mapper2 = GeographicMapper()
    print(mapper2.map_coordinates(40.7128, -74.0060))