from typing import Union
def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number & 1 == 0
if __name__ == '__main__':
    test_cases = [42, -5, 0, 17]
    for value in test_cases:
        result = is_even(value)
        print(f"is_even({value}) = {result}")