import sys
def sanitize_input(data):
    return [float(x) for x in data]
def report_error(error_type, message):
    print(f"[{sys.time()}] ERROR: {error_type}: {message}", file=sys.stderr)
    sys.exit(1)
def find_maximum(values):
    try:
        sanitized = sanitize_input(values)
    except Exception as e:
        report_error("ConversionError", str(e))
    if len(sanitized) == 0:
        report_error("EmptyListError", "The input list cannot be empty.")
    return max(sanitized)
if __name__ == '__main__':
    sample_data = [1, -5.2, '3', 4.8]
    result = find_maximum(sample_data)
    print(f"Maximum value: {result}")