from typing import Union
def is_even(value: Union[int, float]) -> bool:
    try:
        int_value = int(float(value))
    except (ValueError, TypeError):
        return False
    return int_value % 2 == 0
if __name__ == '__main__':
    test_cases = [4.7, -10, "6", None]
    for case in test_cases:
        result = is_even(case)
        print(f"is_even({case!r}) => {result}")