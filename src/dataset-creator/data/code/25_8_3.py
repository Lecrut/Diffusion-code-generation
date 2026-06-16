import logging
from typing import Tuple, Optional
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
def validate_wgs84(lat: float, lon: float) -> bool:
    if not (-90 <= lat <= 90):
        return False
    if not (-180 <= lon <= 180):
        return False
    return True
class LocationValidator:
    def __init__(self):
        self.valid_locations = {(-45.0, -73.6) : "Rio de Janeiro", (29.76, -95.37) : "Houston"}
    def get_name(self, lat: float, lon: float) -> Optional[str]:
        if not validate_wgs84(lat, lon):
            logger.warning(f"Invalid WGS84 coordinates provided: {lat}, {lon}")
            return None
        key = (round(lat, 2), round(lon, 2))
        if key in self.valid_locations:
            name = self.valid_locations[key]
            logger.debug(f"Retrieved location name for {key}: {name}")
            return name
        else:
            logger.warning(f"No known location found at coordinates: {lat}, {lon}")
            return None
if __name__ == '__main__':
    validator = LocationValidator()
    test_cases = [(-45.0, -73.6), (91.0, 0.0), (-20.0, -80.0)]
    for lat, lon in test_cases:
        result = validator.get_name(lat, lon)
        if result is not None:
            print(f"Location at {lat}, {lon}: {result}")