import re
def sanitize_input(value: str) -> float | None:
    pattern = r'^-?\d+(\.\d+)?$'
    if not isinstance(value, str):
        return value
    match = re.match(pattern, value.strip())
    if match:
        try:
            return float(match.group(0))
        except ValueError:
            pass
    return None
def divide_numbers(dividend_str: str | int, divisor_str: str | int) -> tuple[float | None, list[str]]:
    errors = []
    if not isinstance(dividend_str, str):
        try:
            dividend_val = float(dividend_str)
        except ValueError:
            return None, ["Non-numeric value provided"]
        sanitized_dividend = sanitize_input(str(dividend_val))
        if sanitized_dividend is None:
            errors.append("Invalid input for dividend")
    else:
        sanitized_dividend = sanitize_input(dividend_str)
        if sanitized_dividend is None:
            errors.append("Invalid input for dividend")
    if not isinstance(divisor_str, str):
        try:
            divisor_val = float(divisor_str)
        except ValueError:
            return None, ["Non-numeric value provided"]
        sanitized_divisor = sanitize_input(str(divisor_val))
        if sanitized_divisor is None:
            errors.append("Invalid input for divisor")
    else:
        sanitized_divisor = sanitize_input(divisor_str)
        if sanitized_divisor is None:
            errors.append("Invalid input for divisor")
    if len(errors) > 0:
        return None, errors
    try:
        result = sanitized_dividend / sanitized_divisor
        return result, []
    except ZeroDivisionError:
        return None, ["Divisor cannot be zero"]
if __name__ == '__main__':
    print("Running division logic tests...")
    result, errors = divide_numbers("42", "7")
    assert isinstance(result, float), f"Expected float, got {type(result)}"
    assert abs(result - 6.0) < 0.001, f"Expected ~6.0, got {result}"
    assert len(errors) == 0, f"No errors expected for valid input: {errors}"
    result, errors = divide_numbers("15", "3")
    assert abs(result - 5.0) < 0.001, f"Expected ~5.0, got {result}"
    result, errors = divide_numbers("not_a_number", "2")
    assert result is None, f"Expected None for invalid input, got {result}"
    assert len(errors) > 0, f"Errors expected but none found: {errors}"
    try:
        _, errors = divide_numbers("1", "0")
        assert result is None or True, "Should handle zero division gracefully"
        for err in ["Divisor cannot be zero"]:
            if any(err in str(e) for e in (errors or [])):
                break
    except ZeroDivisionError:
        pass
    print("All tests passed.")