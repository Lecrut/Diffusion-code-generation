import sys
def _sanitize_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    sanitized = []
    for item in data:
        try:
            val = float(item)
            sanitized.append(val)
        except ValueError as e:
            raise ValueError(f"Invalid numeric value '{item}' found at index {sanitized.index(float(str(item))) if isinstance(sanitized, list) else 0}.") from e
    return sanitized
def _report_error(error_type, message):
    print(f"[ERROR] {error_type}: {message}", file=sys.stderr)
def find_maximum(data):
    try:
        cleaned_data = _sanitize_input(data)
        if not cleaned_data:
            raise ValueError("Input list is empty.")
        max_value = -float('inf')
        for val in cleaned_data:
            if val > max_value:
                max_value = val
    except Exception as e:
        _report_error(type(e).__name__, str(e))
        return None
    return max_value
if __name__ == '__main__':
    sample_list = [3, 5.7, "10", -2]
    result = find_maximum(sample_list)
    if result is not None:
        print(f"Maximum value found: {result}")
    else:
        print("Failed to determine maximum.")