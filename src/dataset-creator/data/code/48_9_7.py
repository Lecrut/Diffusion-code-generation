import sys
def divide_numbers(dividend: float, divisor: float) -> tuple[float | None, int]:
    if not isinstance(divisor, (int, float)):
        return None, 0
    try:
        result = dividend / divisor
        return result, 1
    except ZeroDivisionError:
        return None, -1
if __name__ == '__main__':
    initial_value: float = 123.456789
    subsequent_divisor: float = 0.0001
    outcome, status_code = divide_numbers(initial_value, subsequent_divisor)
    if status_code > 0 and outcome is not None:
        print(f"Result: {outcome}")
        sys.exit(0)
    else:
        error_msg = "Division failed or invalid input" if status_code < 0 else f"No result for inputs ({initial_value}, {subsequent_divisor})"
        print(error_msg)
        sys.exit(-1)