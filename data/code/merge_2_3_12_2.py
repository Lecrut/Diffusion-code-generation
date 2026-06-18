from typing import Union
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def check_parity_short_circuit(value: Union[int, float]) -> bool:
    if not is_integer(value):
        raise TypeError("Input must be an integer.")
    return value % 2 != 0
def get_parity_status(number: Union[int, float]) -> str:
    if not is_integer(number):
        raise ValueError("Input must be an integer.")
    status = "Even" if check_parity_short_circuit(number) else "Odd"
    return f"The number {number} has {status.lower()} parity."
if __name__ == '__main__':
    test_cases = [10, 7, -3, 42]
    for num in test_cases:
        result_status = get_parity_status(num)
        print(result_status)
        is_odd_result = check_parity_short_circuit(num)
        expected_is_odd = (num % 2 != 0)
        if is_odd_result == expected_is_odd:
            print(f"Verification passed for {num}")
        else:
            print(f"Verification failed for {num}")