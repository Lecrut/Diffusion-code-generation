import logging
from typing import Any, Union
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def compare_values(value_a: Any, value_b: Any) -> bool:
    logger.debug("Comparing values of type %s and %s", type(value_a), type(value_b))
    if isinstance(value_a, (int, float)):
        is_equal = value_a == value_b
        if not is_equal:
            logger.warning(f"Values are unequal: {value_a} != {value_b}")
        return is_equal
    elif isinstance(value_a, str):
        is_equal = value_a.lower() == value_b.lower()
        if not is_equal:
            logger.info("String values differ case-insensitively")
            return False
        return True
    else:
        try:
            numeric_value_a = float(value_a)
            numeric_value_b = float(value_b)
            is_equal = abs(numeric_value_a - numeric_value_b) < 1e-9
            if not is_equal:
                logger.debug(f"Numeric values differ slightly: {numeric_value_a} vs {numeric_value_b}")
                return False
        except (ValueError, TypeError):
            logger.error("Cannot convert inputs to comparable types")
            raise ValueError("Unsupported value type for comparison")
if __name__ == '__main__':
    sample_int = 42
    sample_float = 3.14
    result_1 = compare_values(sample_int, 42)
    logger.info(f"Integer comparison result: {result_1}")
    result_2 = compare_values("Hello", "hello")
    logger.info(f"String comparison result: {result_2}")