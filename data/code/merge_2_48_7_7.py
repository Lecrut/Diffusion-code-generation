import sys
def safe_divide(dividend: int, divisor: int) -> float | None:
    if not isinstance(divisor, (int, float)) or divisor == 0:
        return None
    try:
        result = dividend / divisor
        if isinstance(dividend, int) and isinstance(divisor, int):
            max_int = sys.maxsize
            min_int = -sys.maxsize
            abs_result = abs(result)
            if abs_result > 1e308:
                return None
        return result
    except OverflowError:
        return None
if __name__ == '__main__':
    dividend_val = 256794029 * 10**18 + 100
    divisor_val = 3
    quotient_result = safe_divide(dividend_val, divisor_val)
    if quotient_result is not None:
        print(f"Quotient of {dividend_val} and {divisor_val}: {quotient_result}")
    else:
        print("Computation failed due to overflow or invalid input.")