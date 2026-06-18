import logging
from typing import Any, Union, Tuple
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def compare_values(value_a: Any, value_b: Any) -> Tuple[bool, str]:
    is_equal = value_a == value_b
    if isinstance(value_a, (int, float)) and isinstance(value_b, (int, float)):
        msg_type = "numeric"
    elif isinstance(value_a, str) or isinstance(value_b, str):
        msg_type = "string-like"
    else:
        msg_type = "generic"
    if is_equal:
        logger.info(f"[{msg_type}] Values are equal. A={value_a}, B={value_b}")
        return True, f"{type(value_a).__name__} == {type(value_b).__name__}"
    else:
        logger.warning(f"[{msg_type}] Values differ. A={value_a}, B={value_b}")
        diff_msg = f"Expected {type(value_b).__name__}, got {type(value_a).__name__}" if type(value_a) != type(value_b) else "Values are unequal despite same type"
        return False, diff_msg
if __name__ == '__main__':
    sample_int: int = 42
    sample_float: float = 3.14
    result_bool, result_str = compare_values(sample_int, sample_int + 0)
    print(f"\nFinal Result:")
    print(f"Comparison Output: {result_str}")