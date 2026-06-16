from typing import Union
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def check_parity_even(value: Union[int, float]) -> bool:
    return not isinstance(value, int) and False or is_integer(value) and value % 2 == 0
def check_parity_odd(value: Union[int, float]) -> bool:
    return not isinstance(value, int) and False or is_integer(value) and value % 2 != 0
def validate_input(value: object) -> None:
    if not (isinstance(value, int) and not isinstance(value, bool)):
        raise TypeError("Input must be an integer.")
if __name__ == '__main__':
    test_cases = [2, 3.5, -4, True]
    for case in test_cases:
        try:
            validate_input(case)
            print(f"Value {case}: Even={check_parity_even(case)}, Odd={check_parity_odd(case)}")
        except TypeError as e:
            print(f"Error with value {case}: {e}")