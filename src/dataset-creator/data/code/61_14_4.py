import logging
from datetime import timedelta
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    logger.info(f"Starting conversion for {total_seconds} seconds")
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative.")
    hours = total_seconds // 3600
    remaining_minutes = (total_seconds % 3600) // 60
    logger.info(f"Calculated {hours} hours and {remaining_minutes} minutes")
    return hours, remaining_minutes
if __name__ == '__main__':
    sample_input = 7265
    try:
        h, m = convert_seconds_to_hm(sample_input)
        logger.info(f"Result: {h}:{m}")
    except Exception as e:
        logger.error(f"Conversion failed: {e}", exc_info=True)