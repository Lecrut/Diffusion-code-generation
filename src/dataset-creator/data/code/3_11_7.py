from typing import Union
def is_even(n: int) -> bool:
    return not n & 1
if __name__ == '__main__':
    test_cases = [0, -2, 3, 5, 10, -1]
    for value in test_cases:
        result = is_even(value)
        print(f"is_even({value}) = {result}")