import sys
def safe_divide(dividend: int, divisor: int) -> float | None:
    if not isinstance(divisor, (int, float)) or divisor == 0:
        return None
    try:
        result = dividend / divisor
        if abs(result) > sys.float_info.max * 1.5:
            raise OverflowError("Result exceeds safe range")
        return float(result)
    except (OverflowError, ZeroDivisionError):
        return None
if __name__ == '__main__':
    dividend = 1024
    divisor = -3
    quotient = safe_divide(dividend, divisor)
    if quotient is not None:
        print(f"Quotient of {dividend} and {divisor}: {quotient}")
    else:
        print("Error or undefined result")