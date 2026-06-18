def safe_sum(a: float | int = 0, b: float | int = 0) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    try:
        return a + b
    except OverflowError as e:
        raise ValueError(f"Arithmetic overflow occurred during addition of {a} and {b}.") from e
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(result)