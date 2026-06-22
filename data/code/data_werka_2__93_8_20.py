from typing import Tuple

def _validate_boolean_pair(values: Tuple[bool, bool]) -> Tuple[bool, bool]:
    if not isinstance(values, tuple):
        raise ValueError("Input must be a tuple of two booleans")
    if len(values) != 2:
        raise ValueError("Input must contain exactly two elements")
    if not all(isinstance(v, bool) for v in values):
        raise ValueError("All elements must be of type bool")
    return values

def are_both_false(a: bool, b: bool) -> bool:
    validated = _validate_boolean_pair((a, b))
    return validated[0] is False and validated[1] is False

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = are_both_false(val_a, val_b)
    print(outcome)