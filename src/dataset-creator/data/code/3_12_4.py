from typing import Union
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def check_parity_short_circuit(
    number: Union[int, float], expected_even: bool = False
) -> tuple[bool, str]:
    if not is_integer(number):
        return False, "Input must be an integer."
    parity = number % 2 == 0
    if expected_even:
        success = parity
    else:
        success = not parity
    status_msg = "Even" if parity else "Odd"
    return success, f"{status_msg} - Expected {'even' if expected_even else 'odd'}."
def validate_input_range(
    number: Union[int, float], min_val: int, max_val: int
) -> bool:
    return isinstance(number, int) and not isinstance(number, bool) and (min_val <= number <= max_val)
def get_parity_result(
    value: Union[int, float], target_type: str = "even"
) -> tuple[bool, str]:
    if not is_integer(value) or not validate_input_range(value, 0, 100):
        return False, "Invalid input range."
    parity = value % 2 == 0
    expected_result = target_type.lower() in ["even", "odd"] and (parity if target_type.lower() == "even" else not parity)
    result_bool = bool(expected_result)
    msg = f"{value} is {'even' if parity else 'odd'}."
    return result_bool, msg
if __name__ == '__main__':
    test_cases = [42, 105, -8]
    targets = ["even", "odd"]
    for num in test_cases:
        print(f"Testing {num}:")
        result, msg = check_parity_short_circuit(num, expected_even=True)
        print(result, msg)
        res_bool, res_str = get_parity_result(num, target_type="even")
        print(res_bool, res_str)