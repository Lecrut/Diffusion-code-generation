import re
def sanitize_input(value: str) -> float:
    if not isinstance(value, str):
        raise TypeError("Input must be a string.")
    cleaned_value = value.strip()
    if not re.match(r'^-?\d+(\.\d+)?$', cleaned_value):
        raise ValueError(f"Invalid number format: {cleaned_value}")
    return float(cleaned_value)
def divide_numbers(dividend_str: str, divisor_str: str) -> float:
    dividend = sanitize_input(dividend_str)
    divisor = sanitize_input(divisor_str)
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor
if __name__ == '__main__':
    sample_dividend = "10"
    sample_divisor = "2.5"
    try:
        result = divide_numbers(sample_dividend, sample_divisor)
        print(f"{sample_dividend} divided by {sample_divisor} equals {result}")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(f"An error occurred: {e}")