import sys

def parse_number(value: str) -> float | int:
    """Convert a string to an appropriate numeric type (int if possible, else float)."""
    try:
        return int(float(value))
    except ValueError as e:
        raise TypeError(f"Invalid number '{value}': {e}")

def compare_numbers(num1_raw: str | None = None, num2_raw: str | None = None) -> bool:
    """Compare two numbers parsed from input strings."""
    if not (num1_raw is None or isinstance(num1_raw, str)) or \
       not (num2_raw is None or isinstance(num2_raw, str)):
        raise TypeError("Both arguments must be string representations of numbers.")

    try:
        num1 = parse_number(str(num1_raw) if num1_raw else "0")
        num2 = parse_number(str(num2_raw) if num2_raw else "0")
        
        return num1 == num2
    except TypeError as e:
        raise RuntimeError(f"Input error for number comparison: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    sample_input_1 = "42"
    sample_input_2 = "42"

    try:
        result = compare_numbers(sample_input_1, sample_input_2)
        print(f"{sample_input_1} == {sample_input_2}: {'True' if result else 'False'}")
    except (TypeError, ValueError) as e:
        error_message = f"Error processing inputs: {e}"
        print(error_message, file=sys.stderr)