from typing import Union
def is_positive(value: Union[int, float]) -> bool:
    return isinstance(value, (int, float)) and value > 0
if __name__ == '__main__':
    test_cases = [1.5, -3, 0, True, False]
    for case in test_cases:
        result = is_positive(case)
        print(f"is_positive({case}) -> {result}")