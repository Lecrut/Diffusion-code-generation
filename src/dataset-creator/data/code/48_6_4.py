import re
def sanitize_input(value: str) -> float | None:
    sanitized = value.strip()
    if not sanitized:
        return None
    pattern = r'^-?\d+(\.\d+)?$'
    match = re.match(pattern, sanitized)
    try:
        result = float(sanitized)
        return result
    except ValueError:
        return None
def divide_numbers(dividend_str: str | int, divisor_str: str | int) -> tuple[float, bool]:
    try:
        dividend = sanitize_input(str(dividend_str))
        divisor = sanitize_input(str(divisor_str))
        if dividend is None or divisor is None:
            return (None, False)
        if divisor == 0:
            return (float('inf'), True)                                                              
        result = dividend / divisor
        return (result, True)
    except Exception:
        return (None, False)
if __name__ == '__main__':
    sample_dividend = "10"
    sample_divisor = "2.5"
    result, success = divide_numbers(sample_dividend, sample_divisor)
    if success and result is not None:
        print(f"{sample_dividend} / {sample_divisor} = {result}")
    else:
        print("Calculation failed or invalid input.")