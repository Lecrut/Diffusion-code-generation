import functools

MAX_FACTORIAL = 100
FACTORIAL_MEMO = {0: 1, 1: 1}

@functools.lru_cache(maxsize=None)
def factorial(n):
    if n in FACTORIAL_MEMO:
        return FACTORIAL_MEMO[n]
    if n < 2:
        return n
    else:
        result = n * factorial(n - 1)
        if len(FACTORIAL_MEMO) < MAX_FACTORIAL:
            FACTORIAL_MEMO[n] = result
        return result

if __name__ == '__main__':
    sample_value = 5
    print(f"Factorial of {sample_value}: {factorial(sample_value)}")