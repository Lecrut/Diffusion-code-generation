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
def divide_numbers(dividend_str: str | int, divisor_str: str | int) -> tuple[float | None, list[str]]:
    errors = []
    dividend = sanitize_input(dividend_str)
    if not isinstance(dividend, (int, float)):
        errors.append("Invalid numerator format.")
        return None, errors
    divisor = sanitize_input(divisor_str)
    if not isinstance(divisor, (int, float)):
        errors.append("Invalid denominator format.")
        return None, errors
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    result = dividend / divisor
    return result, []
if __name__ == '__main__':
    sample_dividend = "10.5"
    sample_divisor = "2"
    try:
        final_result, error_list = divide_numbers(sample_dividend, sample_divisor)
        if isinstance(final_result, float):
            print(f"Result of {sample_dividend} / {sample_divisor}: {final_result}")
        else:
            for err in error_list:
                print(f"Error: {err}")
    except ZeroDivisionError as e:
        print(f"Calculation failed due to division by zero: {e}")