import re
def sanitize_input(value: str) -> float | None:
    pattern = r'^-?\d+(\.\d+)?$'
    if not isinstance(value, str):
        return None
    cleaned_value = value.strip()
    if re.match(pattern, cleaned_value) and float(cleaned_value).is_integer():
        return int(float(cleaned_value))
    try:
        result = float(cleaned_value)
        return result
    except ValueError:
        return None
def divide_numbers(dividend_str: str | None, divisor_str: str | None) -> tuple[float, bool]:
    dividend = sanitize_input(dividend_str) if isinstance(dividend_str, str | None) else float(dividend_str)
    divisor = sanitize_input(divisor_str) if isinstance(divisor_str, str | None) else float(divisor_str)
    try:
        result = dividend / divisor
        return (result, True)
    except ZeroDivisionError:
        return (0.0, False)
def run_tests():
    assert divide_numbers("10", "2") == (5.0, True), "Test 1 failed"
    assert divide_numbers("7", None) == (0.0, False), "Test 2 failed"
    assert divide_numbers(None, "3") == (0.0, False), "Test 3 failed"
    try:
        result = divide_numbers("abc", "1")
        assert not result[1], "Invalid input should fail gracefully"
    except Exception as e:
        pass
    print("All tests passed.")
if __name__ == '__main__':
    sample_dividend = "25.0"
    sample_divisor = "4"
    quotient, success = divide_numbers(sample_dividend, sample_divisor)
    if success:
        print(f"{sample_dividend} divided by {sample_divisor} equals {quotient}")
    else:
        print("Division failed.")