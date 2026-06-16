import logging
from typing import Any, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def compare_values(value_a: Any, value_b: Any) -> bool:
    logger.info(f"Comparing {type(value_a).__name__} '{value_a}' with {type(value_b).__name__} '{value_b}'")
    if isinstance(value_a, (int, float)) and isinstance(value_b, (int, float)):
        result = value_a == value_b
        logger.info(f"Numeric comparison: {result}")
        return result
    elif isinstance(value_a, str) and isinstance(value_b, str):
        result = value_a.lower() == value_b.lower()
        logger.info(f"String case-insensitive comparison: {result}")
        return result
    try:
        numeric_value_a = float(value_a) if not isinstance(value_a, (int, float)) else value_a
        numeric_value_b = float(value_b) if not isinstance(value_b, (int, float)) else value_b
        result = abs(numeric_value_a - numeric_value_b) < 1e-6
        logger.info(f"Float comparison with tolerance: {result}")
        return result
    except ValueError as e:
        logger.error(f"Failed to convert values for float comparison: {e}")
        return False
if __name__ == '__main__':
    sample_a = 42.0
    sample_b = "42"
    is_equal = compare_values(sample_a, sample_b)
    if not is_equal:
        logger.warning("Values are considered different.")
    else:
        logger.info("Values match successfully.")