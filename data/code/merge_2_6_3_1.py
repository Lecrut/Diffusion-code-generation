import json
import logging
from typing import Any
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def safe_string_compare(obj1: Any, obj2: Any) -> int:
    try:
        str_repr_1 = repr(obj1)
        str_repr_2 = repr(obj2)
        if not isinstance(str_repr_1, str):
            raise TypeError(f"Object 1 representation is not a string. Got {type(str_repr_1)}")
        if not isinstance(str_repr_2, str):
            raise TypeError(f"Object 2 representation is not a string. Got {type(str_repr_2)}")
        result = -1
        if str_repr_1 < str_repr_2:
            result = -1
        elif str_repr_1 > str_repr_2:
            result = 1
        else:
            result = 0
        logger.info(f"Comparison result for {obj1} and {obj2}: {result}")
        return result
    except Exception as e:
        error_msg = f"Error during comparison of {type(obj1).__name__} and {type(obj2).__name__}: {str(e)}"
        logger.error(error_msg)
        raise
if __name__ == '__main__':
    sample_1 = {"key": "value_a", "nested": [1, 2]}
    sample_2 = {"key": "value_b", "nested": [3, 4]}
    try:
        comparison_result = safe_string_compare(sample_1, sample_2)
        if comparison_result > 0:
            print(f"Object {sample_1} is greater than Object {sample_2}")
        elif comparison_result < 0:
            print(f"Object {sample_1} is less than Object {sample_2}")
        else:
            print("Objects are equal based on string representation")
    except Exception as e:
        logger.critical(f"Fatal error in main execution: {e}")