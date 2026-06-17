import sys
def _sanitize_input(data):
    return [float(x) for x in data]
def _report_error(message):
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)
def find_maximum(values):
    sanitized = _sanitize_input(values)
    if not sanitized:
        _report_error("Input list cannot be empty.")
    return max(sanitized)
if __name__ == '__main__':
    sample_data = [10, 25.5, -3, 42]
    result = find_maximum(sample_data)
    print(f"Maximum value: {result}")