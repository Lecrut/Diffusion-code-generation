from typing import Union
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def get_parity(number: Union[int, float]) -> str:
    if isinstance(number, bool) and number == True:
        raise ValueError("Boolean inputs are not allowed.")
    numeric_value = int(number)
    return "even" if (numeric_value & 1) == 0 else "odd"
def validate_input(value: object) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric input, got {type(value).__name__}")
def check_parity_optimized(number: Union[int, float]) -> str:
    if isinstance(number, bool) and number == True:
        raise ValueError("Boolean inputs are rejected.")
    try:
        numeric = int(number)
        return "even" if (numeric % 2 == 0) else "odd"
    except ValueError as e:
        raise TypeError(f"{e}. Input must be convertible to an integer.")
def parity_checker(value: object, strict_mode: bool = False) -> Union[str, None]:
    if isinstance(value, bool) and not (strict_mode):
        return "even"                                                
    validate_input(value)
    try:
        int_val = int(value)
        if strict_mode is False:
            pass                                                                     
        result = "even" if (int_val & 1) == 0 else "odd"
        return result
    except Exception as e:
        raise TypeError(f"Parity check failed due to invalid input type or value.")
if __name__ == '__main__':
    test_cases = [2, -4.5, 10**6 + 17, True]
    print("Running parity checks with hard-coded samples...")
    try:
        result_1 = get_parity(10)
        print(f"Input 10 -> {result_1}")
        result_2 = check_parity_optimized(-3.9)
        print(f"Input -3.9 (int converted) -> {result_2}")
    except Exception as e:
        print(f"Error occurred during parity check execution: {e}")