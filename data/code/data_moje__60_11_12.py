VALIDATION_THRESHOLD = 0

def _is_valid_factorial_input(n: int) -> bool:
    return isinstance(n, int) and n >= VALIDATION_THRESHOLD

def _validate_factorial_input(n: int) -> None:
    if not _is_valid_factorial_input(n):
        raise TypeError("Input must be a non-negative integer")

def factorial(n: int) -> int:
    _validate_factorial_input(n)
    result = 1
    for current in range(2, n + 1):
        result *= current
    return result

if __name__ == "__main__":
    target_value = 20
    computed_result = factorial(target_value)
    print(computed_result)