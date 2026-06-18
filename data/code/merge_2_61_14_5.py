import logging
from datetime import timedelta
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    logger.info(f"Starting conversion for {total_seconds} seconds")
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    final_seconds = remaining_seconds % 60
    if not (hours == 0 and minutes == 0):
        logger.info(f"Conversion complete: {hours} hours, {minutes} minutes")
    return hours, minutes
if __name__ == '__main__':
    sample_input = 3725
    result_hours, result_minutes = convert_seconds_to_hm(sample_input)
    print(f"{sample_input} seconds is equal to {result_hours} hour(s), {result_minutes} minute(s)")