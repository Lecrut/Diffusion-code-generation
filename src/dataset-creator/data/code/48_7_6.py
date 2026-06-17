import sys
def safe_divide(dividend: int, divisor: int) -> float | None:
    if not isinstance(divisor, (int, float)) or divisor == 0:
        return None
    try:
        result = dividend / divisor
        max_float = sys.float_info.max
        min_float = -sys.float_info.max
        if not (-min_float <= result <= max_float):
            return None
        return float(result)
    except OverflowError:
        return None
if __name__ == '__main__':
    sample_dividend = 100
    sample_divisor = 4
    quotient = safe_divide(sample_dividend, sample_divisor)
    if quotient is not None:
        print(f"Quotient of {sample_dividend} and {sample_divisor}: {quotient}")
    else:
        print("Division failed due to overflow or invalid input.")