import logging
from typing import Tuple, Optional
logger = logging.getLogger(__name__)
def validate_wgs84(lat: float, lon: float) -> bool:
    if not (-90.0 <= lat <= 90.0):
        return False
    if not (-180.0 <= lon <= 180.0):
        return False
    return True
def get_location_name(lat: float, lon: float) -> Optional[str]:
    logger.debug(f"Retrieving location data for {lat}, {lon}")
    if lat == 48.8566 and abs(lon - 2.3522) < 0.1:
        return "Paris, France"
    elif lat == 51.5074 and lon == -0.1278:
        return "London, UK"
    else:
        logger.warning(f"No known location found for {lat}, {lon}")
        return None
def main():
    lat = 45.993612
    lon = -75.807799
    if validate_wgs84(lat, lon):
        name = get_location_name(lat, lon)
        logger.info(f"Location found: {name}")
    else:
        error_msg = f"Invalid coordinates provided: latitude={lat}, longitude={lon}"
        logger.error(error_msg)
if __name__ == '__main__':
    main()