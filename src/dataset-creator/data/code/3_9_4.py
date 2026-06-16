import re
def is_even(value: int) -> bool:
    sanitized_input = str(value).strip() if isinstance(value, (int, float)) else value
    try:
        numeric_value = float(sanitized_input)
        return abs(numeric_value - round(numeric_value)) < 1e-9 and round(numeric_value) % 2 == 0
    except ValueError:
        raise TypeError(f"Invalid input type or format for parity check. Expected a number, got {type(value).__name__}")
if __name__ == '__main__':
    test_cases = [42, -15, "3", "abc", None]
    results = []
    for case in test_cases:
        try:
            result = is_even(case)
            results.append(f"Input {case!r}: {'Even' if result else 'Odd'}")
        except Exception as e:
            results.append(f"Input {case!r}: Error - {e}")
    for res in results:
        print(res)