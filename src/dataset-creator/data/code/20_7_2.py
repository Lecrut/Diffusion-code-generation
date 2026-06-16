import sys
def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError(f"Invalid element type {type(item).__name__}. All elements must be numeric.")
def filter_negative_numbers(data):
    validate_input(data)
    return [x for x in data if x < 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 20, -7, "invalid", None]
    try:
        result = filter_negative_numbers(sample_data)
        print(f"Filtered negative numbers: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error processing input: {e}", file=sys.stderr)