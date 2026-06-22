FACTORIAL_MIN_VALUE = 0
DEFAULT_INIT_FACTOR = 1
ITERATION_START_OFFSET = 2

def factorial(n):
    if n < FACTORIAL_MIN_VALUE:
        raise ValueError("Input must be non-negative")
    accumulated = DEFAULT_INIT_FACTOR
    current = ITERATION_START_OFFSET
    while current <= n:
        accumulated *= current
        current += 1
    return accumulated

if __name__ == '__main__':
    test_values = [0, 5, 10, 20]
    for val in test_values:
        computed = factorial(val)
        print(f"factorial({val}) = {computed}")