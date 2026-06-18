import sys
def safe_divide(dividend: int, divisor: int) -> tuple[int | float]:
    if not isinstance(divisor, (int, float)) or divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")
    try:
        result = dividend // divisor
        remainder = dividend % divisor
        return int(result), int(remainder) if isinstance(dividend, int) else float(result), None
    except OverflowError as e:
        raise ValueError(f"Integer overflow detected during division. {e}")
if __name__ == '__main__':
    a = 100
    b = 4
    try:
        quotient_int, remainder_int, error_msg = safe_divide(a, b) if isinstance(b, int) else (a / b, None, "N/A")
        q, r = divmod(int(a), int(b))
        print(f"Quotient: {q}")
        if error_msg != "N/A":
            print(error_msg)
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)