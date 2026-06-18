from typing import Union
def is_even(number: int) -> bool:
    return isinstance(number, int) and (number & 1 == 0)
if __name__ == '__main__':
    test_cases = [42, -3, 0, 7, 100]
    for value in test_cases:
        result = is_even(value)
        print(f"Number {value} is {'even' if result else 'odd'}")