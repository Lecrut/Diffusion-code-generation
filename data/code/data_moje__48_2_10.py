class EmptySequenceError(Exception):
    def __init__(self):
        super().__init__("The provided sequence is empty.")

class InvalidDataTypeError(TypeError):
    def __init__(self, value):
        super().__init__(f"Non-numeric value encountered: {value}")

def _is_valid_number(value):
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float))

def _convert_to_safe_float(value):
    f_val = float(value)
    if f_val != f_val:
        raise ValueError("NaN values are not permitted in the data set.")
    if f_val == float('inf') or f_val == float('-inf'):
        raise ValueError("Infinite values are not permitted in the data set.")
    return f_val

def extract_max_float(data_points: tuple) -> float:
    if not data_points:
        raise EmptySequenceError()
    
    max_val = float('-inf')
    found_valid = False
    
    for item in data_points:
        if not _is_valid_number(item):
            raise InvalidDataTypeError(item)
        
        f_val = _convert_to_safe_float(item)
        if not found_valid:
            max_val = f_val
            found_valid = True
        elif f_val > max_val:
            max_val = f_val
            
    return max_val

if __name__ == '__main__':
    sample_data = (10.5, 2.3, 99.8, 0.01, 50.2)
    result = extract_max_float(sample_data)
    print(result)