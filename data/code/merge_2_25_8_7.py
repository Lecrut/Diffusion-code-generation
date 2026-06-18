import logging
from typing import Tuple, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_wgs84(lat: float, lon: float) -> bool:
    if not (-90 <= lat <= 90):
        return False
    if not (-180 <= lon <= 180):
        return False
    logger.debug("Coordinate validation passed for (%s, %s)", lat, lon)
    return True
def get_location_name(lat: float, lon: float) -> Optional[str]:
    if validate_wgs84(lat, lon):
        logger.info(f"Retrieving location data for coordinates ({lat}, {lon})")
        return f"Location at {lat:.2f}N/W{abs(lon):.2f}E"
    else:
        raise ValueError("Coordinates are outside WGS84 limits.")
if __name__ == '__main__':
    sample_lat = 51.5074
    sample_lon = -0.1278
    try:
        result = get_location_name(sample_lat, sample_lon)
        print(result)
    except ValueError as e:
        logger.error(f"Validation failed: {e}")