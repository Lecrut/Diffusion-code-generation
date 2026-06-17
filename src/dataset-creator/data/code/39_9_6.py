import sys
def _sanitize_input(data):
    return [float(x) for x in data]
def _report_error(error_type: str, message: str) -> None:
    print(f"[ERROR {error_type}] {message}", file=sys.stderr)
def find_maximum(data):
    if not isinstance(data, list):
        _report_error("TYPE", "Input must be a list.")
        raise TypeError("Expected 'list', got {type(data).__name__}")
    sanitized = _sanitize_input(data)
    if len(sanitized) == 0:
        _report_error("VALUE", "The input list is empty and has no maximum value.")
        raise ValueError("Cannot find max of an empty sequence")
    return float(max(sanitized))
if __name__ == '__main__':
    sample_data = [1, -5.2, 3.7, '0', 4]
    try:
        result = find_maximum(sample_data)
        print(f"Maximum value found: {result}")
    except (TypeError, ValueError) as e:
        _report_error("RUNTIME", str(e))