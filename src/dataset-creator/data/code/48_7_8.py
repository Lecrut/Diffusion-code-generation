import sys
def safe_divide(dividend: int, divisor: int) -> float | None:
    if not isinstance(divisor, (int, float)) or divisor == 0:
        return None
    try:
        result = dividend / divisor
        max_float = sys.float_info.max
        min_float = -sys.float_info.max
        if not (-min_float <= result <= max_float):
            return float('inf') if result > max_float else float('-inf')
        return result
    except OverflowError:
        return None
if __name__ == '__main__':
    dividend_val = 10**308 + 50
    divisor_val = 2
    quotient_result = safe_divide(dividend_val, divisor_val)
    if quotient_result is not None:
        print(f"Quotient of {dividend_val} and {divisor_val}: {quotient_result}")
    else:
        print("Division failed due to overflow or invalid input.")