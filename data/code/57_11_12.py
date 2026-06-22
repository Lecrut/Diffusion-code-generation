from functools import lru_cache

INDEX_TARGET = 30
BASE_ZERO = 0
BASE_ONE = 1

@lru_cache(maxsize=None)
def compute_fibonacci(index: int) -> int:
    if index < BASE_ZERO:
        raise ValueError("Index cannot be negative")
    if index == BASE_ZERO:
        return BASE_ZERO
    if index == BASE_ONE:
        return BASE_ONE
    return compute_fibonacci(index - 1) + compute_fibonacci(index - 2)

if __name__ == '__main__':
    result = compute_fibonacci(INDEX_TARGET)
    print(result)