class EmptySequenceException(Exception):
    def __init__(self, message="Sequence is empty"):
        super().__init__(message)

class TypeValidationError(Exception):
    def __init__(self, message="Invalid type found"):
        super().__init__(message)

def is_valid_float(value):
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float))

def extract_max_float(data_points):
    if not data_points:
        raise EmptySequenceException("Sequence is empty")
    
    if not all(is_valid_float(x) for x in data_points):
        raise TypeValidationError("All items must be numeric")
    
    return max(float(x) for x in data_points)

if __name__ == '__main__':
    test_data = (1.1, 2.2, 3.3, 0.5, 9.9)
    result = extract_max_float(test_data)
    print(result)