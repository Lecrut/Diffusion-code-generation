import logging
from typing import Tuple, Optional
logger = logging.getLogger(__name__)
def validate_wgs84_coords(lat: float, lon: float) -> bool:
    if not (-90 <= lat <= 90):
        return False
    if not (-180 <= lon <= 180):
        return False
    return True
class LocationService:
    def __init__(self):
        self._locations = {}
    def add_location(self, name: str, lat: float, lon: float) -> None:
        if not validate_wgs84_coords(lat, lon):
            logger.warning(f"Invalid coordinates for {name}: ({lat}, {lon})")
            return
        self._locations[name] = (lat, lon)
    def get_location(self, name: str) -> Optional[Tuple[float, float]]:
        if not validate_wgs84_coords(*self._locations.get(name)):
            logger.warning(f"Location '{name}' has invalid coordinates")
            return None
        return self._locations[name]
if __name__ == '__main__':
    service = LocationService()
    service.add_location("New York", 40.7128, -74.0060)
    service.add_location("Invalid North", 95.0, -74.0060)
    service.add_location("Valid South", -33.8688, 151.2093)
    target_name = "New York"
    coords = service.get_location(target_name)
    if coords:
        logger.info(f"Fetched coordinates for {target_name}: {coords}")