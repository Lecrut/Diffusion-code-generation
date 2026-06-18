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
        short_circuit_result = parity
    else:
        short_circuit_result = not parity
    message = (
        f"Number {number} is {'even' if parity else 'odd'} "
        + ("as expected." if short_circuit_result else "unexpected.")
    )
    return bool(short_circuit_result), message
def validate_input_range(
    number: Union[int, float], min_val: int = 0, max_val: None = None
) -> tuple[bool, str]:
    if not isinstance(number, (int, float)):
        return False, "Input must be numeric."
    try:
        int_number = int(number)
    except ValueError:
        return False, "Float values are converted to integers for parity check."
    lower_check = min_val is None or int_number >= min_val
    upper_check = max_val is None or int_number <= max_val
    if not (lower_check and upper_check):
        return False, f"Number {int_number} is outside the range [{min_val}, {max_val}]."
    return True, "Input validation passed."
def run_parity_tests() -> list[tuple]:
    test_cases = [
        (0, False),                     
        (1, True),                     
        (-2, False),                    
        (3.5, None),                                                         
        (4, False),                                      
    ]
    results = []
    for number, exp_even in test_cases:
        valid_range, range_msg = validate_input_range(number)
        parity_result, parity_msg = check_parity_short_circuit(number, expected_even=exp_even if exp_even is not None else False)
        if isinstance(number, float):
            int_number = int(number)
            valid_range, range_msg = validate_input_range(int_number)
        results.append((valid_range, parity_result))
    return results
if __name__ == '__main__':
    test_results = run_parity_tests()
    print("Parity Check Results:")
    for i, (range_valid, parity_ok) in enumerate(test_results):
        status = "PASS" if range_valid and parity_ok else "FAIL"
        print(f"Test {i+1}: Status={status}")