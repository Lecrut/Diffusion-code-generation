from functools import lru_cache

ZERO = 0
ONE = 1
TARGET_INDEX = 50

@lru_cache(maxsize=None)
def compute_fibonacci_value(index: int) -> int:
    if index < ZERO:
        raise ValueError("Index must be non-negative")
    if index == ZERO:
        return ZERO
    if index == ONE:
        return ONE
    first_term = index - ONE
    second_term = index - TWO
    val_a = compute_fibonacci_value(first_term)
    val_b = compute_fibonacci_value(second_term)
    return val_a + val_b

TWO = 2

if __name__ == '__main__':
    output = compute_fibonacci_value(TARGET_INDEX)
    print(output)