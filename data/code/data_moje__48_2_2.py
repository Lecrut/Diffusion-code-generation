class EmptySequenceError(Exception):
    def __init__(self, msg="Sequence is empty"):
        super().__init__(msg)

def validate_numeric(val):
    if isinstance(val, bool):
        raise TypeError(f"Expected numeric, got {type(val).__name__}")
    if not isinstance(val, (int, float)):
        raise TypeError(f"Expected numeric, got {type(val).__name__}")
    if val != val:
        raise ValueError("NaN values are not allowed")
    return float(val)

def extract_max_float(data_points):
    if not data_points:
        raise EmptySequenceError()
    max_val = None
    for item in data_points:
        numeric_val = validate_numeric(item)
        if max_val is None or numeric_val > max_val:
            max_val = numeric_val
    return max_val

if __name__ == '__main__':
    sample_tuple = (1.1, 2.2, 3.3, 4.4, 5.5)
    print(extract_max_float(sample_tuple))