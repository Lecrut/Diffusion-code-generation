import math
def safe_divide(dividend: float | int, divisor: float) -> float:
    if isinstance(dividend, bool):
        raise TypeError("Dividend must be a number (int or float), boolean rejected.")
    if not isinstance(divisor, (float | int)):
        raise TypeError(f"Invalid divisor type: {type(divisor).__name__}. Expected numeric value.")
    try:
        d = float(dividend)
        divs = float(divisor)
        if not math.isfinite(d):
            raise ValueError("Dividend must be a finite number.")
        if not math.isfinite(divs):
            raise ValueError("Divisor cannot be infinite or NaN.")
    except OverflowError:
        raise ValueError(f"Input value overflowed during conversion to float: {dividend}")
    result = d / divs
    if not math.isfinite(result):
        raise ValueError("Division resulted in an infinite or NaN value.")
    return result
if __name__ == '__main__':
    sample_dividend: int | float = 42.5
    sample_divisor: float = 7
    try:
        quotient = safe_divide(sample_dividend, sample_divisor)
        print(f"Quotient of {sample_dividend} divided by {sample_divisor} is {quotient}")
    except (TypeError, ValueError) as exc:
        error_msg = f"{type(exc).__name__}: {exc}"
        raise RuntimeError(error_msg) from None