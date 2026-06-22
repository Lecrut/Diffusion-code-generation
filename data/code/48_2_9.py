class EmptySequenceError(Exception):
    def __init__(self, message="The data sequence is empty."):
        super().__init__(message)

def _is_valid_numeric(value):
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float))

def extract_max_float(data_points: tuple) -> float:
    if not data_points:
        raise EmptySequenceError()
    
    max_value = float('-inf')
    found_value = False
    
    for point in data_points:
        if not _is_valid_numeric(point):
            raise TypeError(f"Invalid type encountered: {type(point).__name__}")
        
        current_val = float(point)
        
        if current_val != current_val:
            raise ValueError("NaN values are not permitted in data points.")
        
        if not found_value or current_val > max_value:
            max_value = current_val
            found_value = True
    
    if not found_value:
        raise ValueError("No valid numeric values found in the sequence.")
        
    return max_value

if __name__ == '__main__':
    sample_tuple = (10.5, 42.1, 3.14, 15.9, 88.0)
    result = extract_max_float(sample_tuple)
    print(result)