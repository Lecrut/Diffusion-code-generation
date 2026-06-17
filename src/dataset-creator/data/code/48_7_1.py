import sys
def safe_divide(dividend: float, divisor: float) -> tuple[float | None]:
    if not isinstance(divisor, (int, float)):
        return None
    try:
        result = dividend / divisor
        max_float = sys.float_info.max
        min_float = -sys.float_info.max
        if abs(result) > max_float or abs(result) < min_float * 1e-308:
            return None
        return result, True
    except ZeroDivisionError:
        return None, False
    except OverflowError:
        return None, False
if __name__ == '__main__':
    dividend = 15.75
    divisor = -2
    quotient_result, is_valid = safe_divide(dividend, divisor)
    if is_valid and quotient_result is not None:
        print(f"Quotient of {dividend} divided by {divisor}: {quotient_result}")
    else:
        print("Error or Overflow detected.")