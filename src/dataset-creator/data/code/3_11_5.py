from typing import Union
def is_even(n: int) -> bool:
    return n & 1 == 0
if __name__ == '__main__':
    test_cases = [1, -2, 3.5, 0]
    for value in test_cases:
        try:
            result = is_even(value) if isinstance(value, int) else "Invalid input type"
            print(f"is_even({value}) -> {result}")
        except Exception as e:
            print(f"is_even({value}) raised an error: {e}")