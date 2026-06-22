from typing import Any

def _validate_boolean_input(value: Any) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return value

def flip_bool_value(value: bool) -> bool:
    is_valid = _validate_boolean_input(value)
    return not is_valid

if __name__ == '__main__':
    true_result = flip_bool_value(True)
    false_result = flip_bool_value(False)
    print(true_result)
    print(false_result)