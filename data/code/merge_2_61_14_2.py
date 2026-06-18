import logging
from datetime import timedelta
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    logger.info(f"Starting conversion for {total_seconds} seconds")
    hours = total_seconds // 3600
    remaining_minutes = (total_seconds % 3600) // 60
    logger.debug(f"Calculated: {hours} hours, {remaining_minutes} minutes")
    return hours, remaining_minutes
if __name__ == '__main__':
    sample_input = 9845
    result_hours, result_minutes = convert_seconds_to_hm(sample_input)
    print(f"{sample_input} seconds is equal to {result_hours} hours and {result_minutes} minutes")