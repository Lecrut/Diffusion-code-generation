def compute_power(base: float, exponent: float) -> float:
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types.")
    if base < 0 and not isinstance(exponent, int):
        raise ValueError("Negative base requires an integer exponent.")
    return base ** exponent

if __name__ == '__main__':
    result = compute_power(2, 10)
    print(result)
    try:
        compute_power(-2, 0.5)
    except ValueError as e:
        print(f"Caught expected error: {e}")