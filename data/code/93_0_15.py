from typing import Tuple
import functools

def validate_boolean_inputs(values: Tuple[bool, bool]) -> Tuple[bool, bool]:
    if not isinstance(values, tuple):
        raise ValueError("Expected a tuple of two boolean values")
    if len(values) != 2:
        raise ValueError("Expected exactly two boolean values")
    first, second = values
    if not isinstance(first, bool) or not isinstance(second, bool):
        raise ValueError("All inputs must be boolean types")
    return (first, second)

def both_are_false(a: bool, b: bool) -> bool:
    validated = validate_boolean_inputs((a, b))
    first_val, second_val = validated
    neg_first = not first_val
    neg_second = not second_val
    return neg_first and neg_second

if __name__ == '__main__':
    x = False
    y = False
    result = both_are_false(x, y)
    print(result)