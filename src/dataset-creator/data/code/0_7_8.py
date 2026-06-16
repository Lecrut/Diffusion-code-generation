import logging
from typing import Any, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def compare_values(value_a: Any, value_b: Any) -> bool:
    logger.info(f"Comparing {type(value_a).__name__} '{value_a}' with {type(value_b).__name__} '{value_b}'")
    if isinstance(value_a, (int, float)) and isinstance(value_b, (int, float)):
        result = value_a == value_b
        logger.info(f"Numeric comparison: {result}")
    elif isinstance(value_a, str) and isinstance(value_b, str):
        result = value_a.lower() == value_b.lower()
        logger.info(f"String case-insensitive comparison: {result}")
    else:
        try:
            numeric_value_a = float(str(value_a))
            numeric_value_b = float(str(value_b))
            result = abs(numeric_value_a - numeric_value_b) < 1e-9
            logger.info(f"Float approximation comparison: {result}")
        except ValueError:
            result = value_a == value_b
            logger.warning("Falling back to exact equality for non-numeric types")
    return result
if __name__ == '__main__':
    sample_int_1 = 42
    sample_float_1 = 3.14159
    sample_str_1 = "Hello"
    sample_list_1 = [1, 2, 3]
    sample_int_2 = 42
    sample_float_2 = 3.14160
    sample_str_2 = "HELLO"
    sample_list_2 = [1, 2, 3]
    result_a = compare_values(sample_int_1, sample_int_2)
    print(f"Integer comparison result: {result_a}")
    result_b = compare_values(sample_float_1, sample_float_2)
    print(f"Float approximation comparison result: {result_b}")
    result_c = compare_values(sample_str_1, sample_str_2)
    print(f"String case-insensitive comparison result: {result_c}")
    result_d = compare_values(sample_list_1, sample_list_2)
    print(f"List equality comparison result: {result_d}")