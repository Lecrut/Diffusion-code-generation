from typing import Union
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def check_parity_short_circuit(
    number: object, target_even: bool = False
) -> tuple[bool, Union[int, str]]:
    if not is_integer(number):
        return (False, "Input must be an integer")
    parity = number % 2 == 0
    if target_even:
        result = parity
        message = f"{number} is {'even' if parity else 'odd'}"
    else:
        result = not parity
        message = f"{number} is {'odd' if not parity else 'even'}"
    return (result, message)
def validate_input(value: object) -> bool:
    try:
        int(value)
        return isinstance(int(value), int) and not isinstance(int(value), bool)
    except ValueError:
        return False
if __name__ == '__main__':
    test_cases = [10, 7, -3.5, "42", True]
    print("Running parity checks with short-circuit evaluation:\n")
    for val in test_cases:
        result_msg = check_parity_short_circuit(val)
        if isinstance(result_msg[0], bool):
            status = "Valid"
        else:
            status = f"{result_msg}"
        print(f"Input: {val} | Status: {status}")
    even_check, msg_even = check_parity_short_circuit(10, target_even=True)
    odd_check, msg_odd = check_parity_short_circuit(9, target_even=False)
    print(f"\nSpecific Tests:")
    print(f"Even Check (target=even): {msg_even} | Result: {'PASS' if even_check else 'FAIL'}")
    print(f"Odd Check (target=odd): {msg_odd} | Result: {'PASS' if odd_check else 'FAIL'}")