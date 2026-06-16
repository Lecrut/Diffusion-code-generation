from typing import Any
def is_even(number: int) -> bool:
    return number % 2 == 0
if __name__ == '__main__':
    test_values = [10, -5, 0, 3]
    for val in test_values:
        result_val = is_even(val)
        print(f"Number {val} -> Even: {result_val}")