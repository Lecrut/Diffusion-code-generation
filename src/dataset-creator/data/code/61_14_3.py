import logging
from functools import wraps
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully. Result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper
@log_execution
def seconds_to_hms(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative.")
    hours = int(total_seconds // 3600)
    remaining_minutes = (total_seconds % 3600) // 60
    minutes = int(remaining_minutes)
    seconds = total_seconds - (hours * 3600 + minutes * 60)
    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": round(seconds, 2)
    }
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    sample_inputs = [3601, 7925, 86400]
    for sec in sample_inputs:
        result = seconds_to_hms(sec)
        print(f"Input ({sec}) -> Hours: {result['hours']}, Minutes: {result['minutes']}, Seconds: {result['seconds']}")