def safe_power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be integers or floats")
    if base < 0 and exponent < 0:
        raise ValueError("Negative base with negative exponent is not allowed")
    return base ** exponent

if __name__ == '__main__':
    try:
        result1 = safe_power(2, 3)
        print(result1)
    except (TypeError, ValueError) as e:
        print(e)
    try:
        result2 = safe_power(-2, -3)
        print(result2)
    except (TypeError, ValueError) as e:
        print(e)
    try:
        result3 = safe_power(5, 0)
        print(result3)
    except (TypeError, ValueError) as e:
        print(e)
    try:
        result4 = safe_power("a", 2)
        print(result4)
    except (TypeError, ValueError) as e:
        print(e)