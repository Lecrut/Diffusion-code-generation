import sys
def validate_and_sort_input(values):
    try:
        numeric_values = [float(v) for v in values]
        return sorted(numeric_values)
    except ValueError as e:
        raise TypeError(f"Invalid input provided: {e}") from e
if __name__ == '__main__':
    sample_inputs = ["10", "3.5", "-2", "7", "invalid"]
    for item in sample_inputs:
        try:
            result = validate_and_sort_input([item])
            print(f"Input '{result[0]}', Type: {type(result[0]).__name__}")
        except TypeError as e:
            print(f"Error processing input '{item}': {e}", file=sys.stderr)