def sanitize_input(value: str) -> float | None:
    try:
        return float(value) if value.strip() else 0.0
    except ValueError:
        raise TypeError(f"Invalid input type for number conversion: {value}")
def divide_numbers(dividend_str: str = "10", divisor_str: str = "2") -> tuple[float, bool]:
    dividend = sanitize_input(dividend_str)
    divisor = sanitize_input(divisor_str)
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Input values must be convertible to numbers.")
    if divisor == 0:
        return None, False
    result = dividend / divisor
    return result, True
if __name__ == '__main__':
    sample_dividend = "15"
    sample_divisor = "3"
    try:
        result, success = divide_numbers(sample_dividend, sample_divisor)
        if not success:
            print("Division failed.")
        else:
            assert isinstance(result, float), "Result must be a float."
            formatted_result = f"{result:.2f}"
            print(f"Calculated result of {sample_dividend} / {sample_divisor}: {formatted_result}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"An error occurred during calculation: {e}")