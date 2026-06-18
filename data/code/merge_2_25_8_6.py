import logging
from typing import Tuple, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_wgs84_coordinate(coord: float) -> bool:
    return -180 <= coord <= 180
def get_location_name(lat: float, lon: float) -> str:
    if not (validate_wgs84_coordinate(lat) and validate_wgs84_coordinate(lon)):
        raise ValueError("Coordinates out of WGS84 limits")
    logger.debug(f"Retrieving name for lat={lat}, lon={lon}")
    return f"Location at {lat:.2f}N, {lon:.2f}E"
if __name__ == '__main__':
    test_lat = 35.6762
    test_lon = -139.8404
    try:
        name = get_location_name(test_lat, test_lon)
        print(name)
        invalid_lat = float('-inf')
        result = validate_wgs84_coordinate(invalid_lat)
        logger.info(f"Validation of {invalid_lat}: {result}")
    except ValueError as e:
        logger.error(str(e))