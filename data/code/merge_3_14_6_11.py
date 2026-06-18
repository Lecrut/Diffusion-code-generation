import sys

def get_value(value_str):
    """Converts a string to a float number."""
    try:
        return float(value_str)
    except ValueError as e:
        raise ValueError(f"Input '{value_str}' is not numeric.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing.
    SAMPLE_VALUE_1 = "10.5"
    SAMPLE_VALUE_2 = "23.4"

    try:
        measurement_a = get_value(SAMPLE_VALUE_1)
        measurement_b = get_value(SAMPLE_VALUE_2)
        
        if measurement_a < measurement_b:
            result_str = f"{measurement_a} is less than {measurement_b}"
        elif measurement_a > measurement_b:
            result_str = f"{measurement_a} is greater than {measurement_b}"
        else:
            result_str = f"{measurement_a} equals {measurement_b}"

        print(result_str)
    except ValueError as e:
        # Since we are using hard-coded values, this block technically shouldn't be reached.
        # However, it handles the case if a hardcoded value were invalid for robustness demonstration.
        print(f"Error occurred while parsing sample data: {e}", file=sys.stderr)
        sys.exit(1)