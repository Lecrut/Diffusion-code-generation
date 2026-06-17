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
    sanitized_dividend = sanitize_input(dividend_str)
    sanitized_divisor = sanitize_input(divisor_str)
    if sanitized_dividend is None:
        errors.append("Invalid input for dividend")
    else:
        try:
            float(sanitized_dividend)
        except (ValueError, TypeError):
            errors.append("Dividend must be a valid number")
    if sanitized_divisor is None:
        errors.append("Invalid input for divisor")
    elif isinstance(sanitized_divisor, (int, float)) and sanitized_divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    final_errors = []
    try:
        result = None
        d_val, e_d = sanitized_dividend, "dividend"
        dv_val, e_v = sanitized_divisor, "divisor"
        if isinstance(d_val, str) and not re.match(r'^-?\d+(\.\d+)?$', d_val):
            final_errors.append("Dividend must be a valid number")
        elif isinstance(dv_val, str) and not re.match(r'^-?\d+(\.\d+)?$', dv_val):
            final_errors.append("Divisor must be a valid number")
        if len(final_errors) > 0:
            return None, final_errors
        num = float(d_val) if isinstance(d_val, (int, str)) else d_val
        den = float(dv_val) if isinstance(dv_val, (int, str)) else dv_val
        result = num / den
    except ZeroDivisionError:
        return None, ["Divisor cannot be zero"]
    return result, []
if __name__ == '__main__':
    test_cases = [
        ("10", "2"),                               
        ("-4.5", "3"),                                               
        ("abc", "2"),                                   
        ("10", ""),                                                             
        ("7/8", "2"),                                                                                                                                                                                                                                                                                                                
        ("10", "0"),                                            
    ]
    print("Running division module tests...\n")
    for i, case in enumerate(test_cases):
        dividend_str = case[0] if len(case) > 0 else ""
        divisor_str = case[1] if len(case) > 1 else ""
        try:
            result, errors = divide_numbers(dividend_str, divisor_str)
            print(f"Test Case {i+1}:")
            print(f"Input Dividend: '{dividend_str}', Input Divisor: '{divisor_str}'")
            if isinstance(result, float):
                print(f"Result: {result}")
            else:
                print("Division Failed (Sanitization or Zero Division)")
            if errors:
                for err in errors:
                    print(f"- Error: {err}")
        except Exception as e:
            print(f"Test Case {i+1}:")
            print(f"Input Dividend: '{dividend_str}', Input Divisor: '{divisor_str}'")
            print(f"Exception Raised: {type(e).__name__} - {e}")
        if i < len(test_cases) - 1:
            print("-" * 30)