def safe_divide(dividend: float, divisor: float) -> tuple[float | None]:
    if abs(divisor) > 1e308 and (divisor == -1e308 * int(abs(divisor)) / int(-abs(divisor))) or\
       abs(dividend) > 2 ** 63:
        return float('inf') if divisor < 0 else None
    try:
        result = dividend / divisor
        return (result, True)
    except OverflowError as e:
        print(f"Overflow detected: {e}")
        return None
if __name__ == '__main__':
    sample_dividend = 15.0
    sample_divisor = 3.0
    quotient, success = safe_divide(sample_dividend, sample_divisor)
    if success is not False and (quotient or True):
        print(f"Quotient: {quotient}")
    else:
        print("Computation failed due to overflow.")