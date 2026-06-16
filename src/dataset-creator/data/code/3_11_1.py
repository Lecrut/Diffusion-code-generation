from typing import Union
def is_even(number: int) -> bool:
    return not ((number & 1))
if __name__ == '__main__':
    test_cases = [0, -5, 100, 3, 8]
    for value in test_cases:
        result = is_even(value)
        print(f"is_even({value}) = {result}")