import re
def sanitize_input(value: str) -> float | None:
    pattern = r'^-?\d+(\.\d+)?$'
    if not isinstance(value, str):
        return value
    match = re.match(pattern, value.strip())
    try:
        return float(match.group(0))
    except ValueError:
        return None
def divide_numbers(dividend_str: str | int, divisor_str: str | int) -> tuple[float | None, bool]:
    dividend = sanitize_input(dividend_str)
    divisor = sanitize_input(divisor_str)
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        return None, True
    try:
        result = dividend / divisor
        return result, False
    except ZeroDivisionError:
        return None, True
if __name__ == '__main__':
    sample_dividend = "10"
    sample_divisor = "2.5"
    result, error_occurred = divide_numbers(sample_dividend, sample_divisor)
    if not error_occurred and isinstance(result, float):
        print(f"{sample_dividend} / {sample_divisor} = {result}")
    else:
        print("Division failed or invalid input.")