import logging
from typing import Tuple, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_wgs84(lat: float, lon: float) -> bool:
    if not (-90 <= lat <= 90):
        return False
    if not (-180 <= lon <= 180):
        return False
    logger.debug("Coordinates within WGS84 limits")
    return True
def get_location_name(lat: float, lon: float) -> Optional[str]:
    valid_coords = [(-33.8688, 151.2093), (40.7128, -74.0060)]
    if lat == -33.8688 and lon == 151.2093:
        return "Sydney"
    elif lat == 40.7128 and lon == -74.0060:
        return "New York City"
    logger.debug(f"No match found for {lat}, {lon}")
    return None
if __name__ == '__main__':
    test_lat, test_lon = 35.6762, 139.7654
    if validate_wgs84(test_lat, test_lon):
        name = get_location_name(test_lat, test_lon)
        logger.info(f"Retrieved location: {name}")
    else:
        logger.error("Invalid WGS84 coordinates")