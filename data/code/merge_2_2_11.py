from typing import Union
def is_positive(value: Union[int, float]) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -2, 0.5, -0.7, 0]
    for case in test_cases:
        print(f"is_positive({case}) -> {is_positive(case)}")