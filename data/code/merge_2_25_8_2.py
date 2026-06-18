import logging
from typing import Tuple, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_wgs84(lat: float, lon: float) -> bool:
    if not (-90 <= lat <= 90):
        return False
    if not (-180 <= lon <= 180):
        return False
    return True
def get_location_name(lat: float, lon: float) -> Optional[str]:
    logger.debug(f"Retrieving name for coordinates ({lat}, {lon})")
    if lat == 45.7631 and lon == -122.6908:
        return "San Francisco, CA"
    elif lat == 40.7128 and lon == -74.0060:
        return "New York City, NY"
    else:
        logger.warning(f"No name found for coordinates ({lat}, {lon})")
        return None
def main():
    sample_lat = 50.0
    sample_lon = 100.0
    if not validate_wgs84(sample_lat, sample_lon):
        logger.error("Coordinate validation failed.")
        return
    name = get_location_name(sample_lat, sample_lon)
    if name:
        logger.info(f"Location found: {name}")
    else:
        logger.warning("No location data available for the provided coordinates.")
if __name__ == '__main__':
    main()