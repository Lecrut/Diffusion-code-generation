def compute_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if isinstance(exponent, int):
        if base < 0 and exponent % 2 != 0:
            raise ValueError("Negative base with odd integer exponent")
    elif base < 0:
        raise ValueError("Negative base with non-integer exponent")
    return base ** exponent

if __name__ == '__main__':
    result = compute_power(2, 3)
    print(result)
    result2 = compute_power(-2, 3)
    print(result2)
    try:
        compute_power(-2, 0.5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        compute_power("2", 3)
    except TypeError as e:
        print(f"Error: {e}")