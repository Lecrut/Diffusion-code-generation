import sys
def safe_sort_numeric(values):
    try:
        coerced = [int(v) for v in values]
        return sorted(coerced)
    except ValueError as e:
        raise TypeError(f"Invalid input provided: {e}") from e
if __name__ == '__main__':
    sample_inputs = ["10", "2.5", "-3", "abc", "", " 4 ", None]
    for item in sample_inputs:
        try:
            result = safe_sort_numeric([str(item)]) if item is not None else []
            print(f"Input {repr(item)} -> Sorted: {result}")
        except Exception as e:
            print(f"Error processing input {repr(item)}: {e}", file=sys.stderr)