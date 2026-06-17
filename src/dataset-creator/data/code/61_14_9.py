import logging
from datetime import timedelta
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def convert_seconds_to_time(total_seconds: int) -> tuple[int, int]:
    logger.debug("Starting conversion process for %d seconds", total_seconds)
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    hours = total_seconds // 3600
    remaining_seconds_after_hours = (total_seconds % 3600) // 60
    minutes = int(remaining_seconds_after_hours)
    logger.info("Conversion complete: %d seconds -> %d hours and %d minutes", 
               total_seconds, hours, minutes)
    return hours, minutes
if __name__ == '__main__':
    sample_seconds = 3665
    try:
        h, m = convert_seconds_to_time(sample_seconds)
        logger.info("Result for input %d seconds:", sample_seconds)
        print(f"{sample_seconds} seconds is {h} hour(s) and {m} minute(s)")
    except ValueError as ve:
        logger.error("%s", ve)
        raise