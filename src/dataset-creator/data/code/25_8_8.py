import logging
from typing import Tuple, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_wgs84(lat: float, lon: float) -> bool:
    if not (-90 <= lat <= 90):
        return False
    if not (-180 <= lon <= 180):
        return False
    logger.debug(f"Coordinates validated successfully for {lat}, {lon}")
    return True
def get_location_name(lat: float, lon: float) -> Optional[str]:
    if not validate_wgs84(lat, lon):
        raise ValueError("Invalid WGS84 coordinates")
    logger.debug(f"Retrieving name for {lat}, {lon}")
    known_locations = {
        (0.0, 175.0),
        (-33.8688, 151.2093)
    }
    if (lat, lon) in known_locations:
        return "Simulated City"
    logger.debug(f"No matching location found for {lat}, {lon}")
    return None
if __name__ == '__main__':
    test_lat = -33.8688
    test_lon = 151.2093
    try:
        name = get_location_name(test_lat, test_lon)
        logger.info(f"Retrieved location name: {name}")
    except ValueError as e:
        logger.error(f"Validation failed: {e}")