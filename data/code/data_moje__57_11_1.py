from functools import lru_cache

BASE_CASES = {0: 0, 1: 1, 2: 1}

@lru_cache(maxsize=None)
def fibonacci(n):
    if n in BASE_CASES:
        return BASE_CASES[n]
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    result = fibonacci(30)
    print(result)