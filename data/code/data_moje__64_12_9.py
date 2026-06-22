import sys

def power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1.0
    if exponent < 0:
        if base == 0.0:
            raise ZeroDivisionError("base cannot be zero when exponent is negative")
        result = 1.0
        for _ in range(-exponent):
            result *= base
        return 1.0 / result
    
    result = 1.0
    for _ in range(exponent):
        if result != 0.0 and abs(base) > sys.float_info.max / abs(result):
            raise OverflowError("Result exceeds float maximum value")
        result *= base
    return result

if __name__ == "__main__":
    try:
        val = power(2.5, 4)
        print(val)
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        val_neg = power(1.0, -3)
        print(val_neg)
    except Exception as e:
        print(f"Error: {e}")

    try:
        val_zero = power(0.0, -1)
        print(val_zero)
    except Exception as e:
        print(f"Error: {e}")

    try:
        val_large = power(100.0, 309)
        print(val_large)
    except Exception as e:
        print(f"Error: {e}")