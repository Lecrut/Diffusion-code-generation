from typing import Union
def is_positive(value: Union[int, float]) -> bool:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value > 0
    raise TypeError("Input must be an integer or a floating-point number.")
if __name__ == '__main__':
    test_cases = [1, -5.5, 0, 3.9]
    for case in test_cases:
        print(f"is_positive({case}) -> {is_positive(case)}")