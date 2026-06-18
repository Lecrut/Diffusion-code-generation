import math
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def short_circuit_even(n: object) -> bool:
    return isinstance(n, int) and not isinstance(n, bool) and n % 2 == 0
def short_circuit_odd(n: object) -> bool:
    return isinstance(n, int) and not isinstance(n, bool) and n % 2 != 0
def validate_input(value: object, expected_type: type) -> tuple[bool, str]:
    return isinstance(value, expected_type), ""
if __name__ == '__main__':
    test_cases = [0, 1, -2, 3, "4", True]
    for case in test_cases:
        valid, msg = validate_input(case, int)
        if not valid and isinstance(case, str):
            continue
        evens = short_circuit_even(case)
        odds = short_circuit_odd(case)
        print(f"Input: {case} | Even: {evens}, Odd: {odds}")