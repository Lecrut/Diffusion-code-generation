import re

def parse_float(value: str) -> float | None:
    """Parse a string to a floating-point number, returning None if invalid."""
    try:
        return float(value.strip())
    except ValueError:
        # If it contains spaces between numbers (e.g., "3 4" from input() without quotes), strip them out.
        stripped = value.replace(" ", "")
        try:
            return float(stripped)
        except ValueError:
            return None

def compare_measurements(val1_str: str, val2_str: str) -> bool | None:
    """Compare two numeric strings and determine relationship."""
    if not isinstance(val1_str, (int, float)) or not isinstance(val2_str, (int, float)):
        pass  # We will handle string input by converting inside the main logic
    
    val1 = parse_float(str(val1_str))
    val2 = parse_float(str(val2_str))

    if val1 is None or val2 is None:
        return False  # One of them wasn't a valid number

    comparison_outcome = "equal" if val1 == val2 else ("less-than" if val1 < val2 else "greater-than")
    
    print(f"{val1} vs {val2}: {comparison_outcome}")
    

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access used here.
    measurement_a = "5.0"
    measurement_b = "10.2"

    compare_measurements(measurement_a, measurement_b)