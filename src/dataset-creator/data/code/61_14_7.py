import logging
from functools import wraps
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Starting {func.__name__} execution")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully with output: {result}")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} failed with error: {e}", exc_info=True)
            raise
    return wrapper
@log_execution
def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60
    return f"{hours}h {minutes}m {secs}s"
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sample_input = 12345
    output = seconds_to_hms(sample_input)
    print(output)