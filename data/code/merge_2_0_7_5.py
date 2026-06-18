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
    else:
        try:
            numeric_value_a = float(str(value_a))
            numeric_value_b = float(str(value_b))
            result = abs(numeric_value_a - numeric_value_b) < 1e-6
            logger.info(f"Float comparison with tolerance: {result}")
            return result
        except ValueError:
            try:
                hash_a = str(hash(str(value_a)))[:8]
                hash_b = str(hash(str(value_b)))[:8]
                if value_a == value_b or (isinstance(value_a, dict) and isinstance(value_b, dict)) or\
                   (isinstance(value_a, list) and isinstance(value_b, list)):
                    result = True
                else:
                    result = False
            except Exception as e:
                logger.error(f"Comparison failed due to type mismatch: {e}")
                return False
    logger.info("Default comparison logic applied")
    return value_a == value_b
if __name__ == '__main__':
    sample_int_1 = 42
    sample_float_1 = 3.14159
    sample_str_1 = "Hello"
    sample_dict_1 = {"key": "value"}
    result_a = compare_values(sample_int_1, 42)
    print(f"Integer comparison result: {result_a}")
    result_b = compare_values(sample_float_1, 3.14159)
    print(f"Float comparison result: {result_b}")
    result_c = compare_values(sample_str_1, "HELLO")
    print(f"String case-insensitive comparison result: {result_c}")
    result_d = compare_values({"key": "value"}, {"KEY": "VALUE"})
    print(f"Dict equality check (case sensitive): {result_d}")