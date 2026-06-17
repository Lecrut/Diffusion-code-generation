from typing import Union
def is_positive(value: Union[int, float]) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5, 0.5, 0, "invalid"]
    for case in test_cases:
        try:
            result = is_positive(case) if isinstance(case, (int, float)) else False
            print(f"is_positive({case}) -> {result}")
        except Exception:
            print(f"Error processing {case}: Invalid input type")