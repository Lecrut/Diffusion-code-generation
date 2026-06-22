class EmptyDataError(Exception):
    def __init__(self):
        super().__init__("The provided data sequence is empty.")

def _validate_and_convert(value):
    if isinstance(value, bool):
        raise TypeError(f"Boolean values are not allowed, got {type(value).__name__}")
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(value).__name__}")
    return float(value)

def extract_max_float(data_points: tuple) -> float:
    if len(data_points) == 0:
        raise EmptyDataError()
    
    current_max = _validate_and_convert(data_points[0])
    
    for i in range(1, len(data_points)):
        candidate = _validate_and_convert(data_points[i])
        if candidate > current_max:
            current_max = candidate
            
    return current_max

if __name__ == '__main__':
    sample_sequence = (10.5, 3.2, 45.0, 2.1, 99.9, -5.5)
    result = extract_max_float(sample_sequence)
    print(result)