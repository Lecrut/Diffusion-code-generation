import logging
from functools import wraps
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully. Result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper
@log_execution
def seconds_to_hm(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours}h {minutes}m {seconds}s"
if __name__ == '__main__':
    import sys
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    test_cases = [3725, 0, 86400]
    for sec in test_cases:
        print(f"Input seconds: {sec}")
        output = seconds_to_hm(sec)
        print(output)