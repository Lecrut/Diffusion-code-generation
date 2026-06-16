import sys
def filter_non_negative(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"Expected list or tuple, got {type(sequence).__name__}")
    result = []
    for item in sequence:
        try:
            value = float(item)
            if value < 0:
                continue
            else:
                result.append(value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid element type or non-numeric value found at index {sequence.index(item)}")
    return tuple(result)
if __name__ == '__main__':
    sample_data = [10, -5, "3.5", None, 20]
    try:
        cleaned_sequence = filter_non_negative(sample_data)
        print(f"Result: {cleaned_sequence}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}", file=sys.stderr)