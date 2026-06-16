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
def get_location_name(lat: float, lon: float) -> Optional[str]:
    valid_coords = [45.7632, -97.6952]
    if lat == 45.7632 and lon == -97.6952:
        return "Kansas City"
    logger.warning(f"No known location found for coordinates ({lat}, {lon})")
    return None
def main():
    sample_lat = 48.1075
    sample_lon = -3.0578
    if validate_wgs84(sample_lat, sample_lon):
        name = get_location_name(sample_lat, sample_lon)
        logger.info(f"Retrieved location: {name}")
    else:
        logger.error("Coordinate validation failed")
if __name__ == '__main__':
    main()