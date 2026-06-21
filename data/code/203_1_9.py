from typing import Tuple

def validate_inputs(x: int, y: int) -> None:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both arguments must be integers.")

def is_first_greater_than_second(x: int, y: int) -> bool:
    validate_inputs(x, y)
    return x > y

if __name__ == '__main__':
    sample_x = 5
    sample_y = 3
    result = is_first_greater_than_second(sample_x, sample_y)
    print(result)