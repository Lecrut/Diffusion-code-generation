import logging
from typing import Any
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def compare_values(value_a: Any, value_b: Any) -> bool | None:
    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
        logger.warning(f"Non-numeric comparison attempted for {type(value_a)} and {type(value_b)}. Returning False.")
        return False
    result = value_a == value_b
    if result:
        logger.info("Values are equal")
    else:
        logger.debug(f"Difference detected between {value_a} and {value_b}")
    return result
if __name__ == '__main__':
    sample_int_1 = 42
    sample_float_3 = 0.5
    is_equal_ints = compare_values(sample_int_1, sample_int_1)
    print(f"Integers equal: {is_equal_ints}")
    result_mixed = compare_values(42, "42")
    print(f"Mixed types equal: {result_mixed}")