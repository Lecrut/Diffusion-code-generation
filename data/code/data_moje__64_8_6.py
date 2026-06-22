def safe_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number.")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number.")
    if base < 0 and exponent < 0:
        raise ValueError("Negative base cannot have a negative exponent.")
    if base < 0 and exponent != int(exponent):
        raise ValueError("Negative base must have an integer exponent.")
    result = base ** exponent
    if isinstance(result, complex) and result.imag != 0:
        raise ValueError("Result is complex.")
    return result

if __name__ == '__main__':
    print(safe_power(2, 3))
    print(safe_power(-2, 3))
    try:
        print(safe_power(-2, -3))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(safe_power(2.0, "2"))
    except TypeError as e:
        print(f"Error: {e}")