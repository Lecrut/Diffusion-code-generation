from typing import Union
def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number % 2 == 0
if __name__ == '__main__':
    test_cases = [10, -4, 3, 0]
    for value in test_cases:
        result = is_even(value)
        print(f"is_even({value}) = {result}")