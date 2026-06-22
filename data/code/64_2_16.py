import math

def raise_power(base: float, exponent: float) -> float:
    if not math.isfinite(base) and base != 0:
        raise ValueError("Base must be finite")
    if not math.isfinite(exponent) and exponent != 0:
        raise ValueError("Exponent must be finite")
    if base == 0 and exponent <= 0:
        raise ValueError("0 cannot be raised to a non-positive exponent")
    return math.pow(base, exponent)

if __name__ == "__main__":
    int_result = raise_power(2, 10)
    float_result = raise_power(2.5, 3.2)
    negative_exp_result = raise_power(5, -2)
    print(int_result)
    print(float_result)
    print(negative_exp_result)