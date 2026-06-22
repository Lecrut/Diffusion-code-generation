from typing import Tuple

POSITIVE_THRESHOLD: int = 0
REQUIRED_POSITIVE_COUNT: int = 2

def evaluate_conditions(a: int, b: int, c: int) -> bool:
    values: Tuple[int, int, int] = (a, b, c)
    positive_count: int = 0
    for val in values:
        if val > POSITIVE_THRESHOLD:
            positive_count += 1
    return positive_count >= REQUIRED_POSITIVE_COUNT

if __name__ == '__main__':
    result: bool = evaluate_conditions(10, -5, 20)
    print(result)