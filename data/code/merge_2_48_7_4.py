import sys
def safe_divide(dividend: int, divisor: int) -> float | None:
    if not isinstance(divisor, (int, float)) or divisor == 0:
        return None
    try:
        result = dividend / divisor
        max_float = sys.float_info.max
        min_float = -sys.float_info.max
        if not (-min_float <= result <= max_float):
            raise OverflowError("Result exceeds float range")
        return result
    except (OverflowError, ZeroDivisionError) as e:
        print(f"Calculation error: {e}", file=sys.stderr)
        return None
if __name__ == '__main__':
    dividend = 10**308 + 50
    divisor = 2
    quotient = safe_divide(dividend, divisor)
    if isinstance(quotient, float):
        print(f"Quotient: {quotient}")