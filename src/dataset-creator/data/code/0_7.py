import logging
from typing import Any, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def compare_values(value_a: Any, value_b: Any) -> bool:
    logger.info(f"Comparing {type(value_a).__name__} '{value_a}' with {type(value_b).__name__} '{value_b}'")
    if isinstance(value_a, (int, float)) and isinstance(value_b, (int, float)):
        result = value_a == value_b
        logger.info(f"Numeric comparison: {result}")
    elif isinstance(value_a, str) or isinstance(value_b, str):
        result = value_a == value_b
        logger.info(f"String comparison: '{value_a}' vs '{value_b}' -> {result}")
    else:
        try:
            result = value_a == value_b
            logger.info(f"Mixed type comparison: {type(value_a).__name__} and {type(value_b).__name__} -> {result}")
        except Exception as e:
            logger.error(f"Error during comparison: {e}", exc_info=True)
    return result
if __name__ == '__main__':
    sample_int = 42
    sample_float = 3.14
    sample_str = "hello"
    compare_values(sample_int, sample_int)
    compare_values(50, float("inf"))
    compare_values(sample_str, sample_str.upper())