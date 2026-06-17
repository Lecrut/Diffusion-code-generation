import sys
def safe_divide(numerator: int, denominator: int) -> float | None:
    if not isinstance(denominator, (int, float)) and not issubclass(type(denominator), type):
        raise TypeError("Denominator must be a number")
    try:
        result = numerator / denominator
        max_int = sys.maxsize if sys.version_info[0] >= 3 else 2**31 - 1
        min_int = -(sys.maxsize) if sys.version_info[0] >= 3 else -2**31
        import math
        if not (math.isfinite(result)):
            return None
        return result
    except OverflowError:
        return None
if __name__ == '__main__':
    num = 100
    deno = 25
    quotient = safe_divide(num, deno)
    if quotient is not None:
        print(f"Quotient of {num} and {deno}: {quotient}")
    else:
        print("Computation resulted in overflow or undefined value.")