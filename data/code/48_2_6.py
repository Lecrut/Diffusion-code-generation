class InvalidDataTypeError(TypeError):
    def __init__(self, value, expected_type):
        super().__init__(f"Expected {expected_type}, got {type(value).__name__} for value {value}")

class EmptyDataError(ValueError):
    def __init__(self):
        super().__init__("Data tuple is empty")

VALID_TYPES = (int, float)
BOOL_TYPES = (bool,)

def extract_maximum_float(data_tuple):
    if not isinstance(data_tuple, tuple):
        raise TypeError(f"Expected tuple, got {type(data_tuple).__name__}")
    if len(data_tuple) == 0:
        raise EmptyDataError()
    
    current_max = None
    index = 0
    
    while index < len(data_tuple):
        item = data_tuple[index]
        
        if isinstance(item, BOOL_TYPES):
            raise InvalidDataTypeError(item, "non-boolean numeric")
        
        if not isinstance(item, VALID_TYPES):
            raise InvalidDataTypeError(item, "numeric")
            
        numeric_value = float(item)
        
        if current_max is None or numeric_value > current_max:
            current_max = numeric_value
            
        index += 1
        
    return current_max

if __name__ == '__main__':
    sample_points = (10.5, 3.2, 8.9, -1.1, 15.0)
    result = extract_maximum_float(sample_points)
    print(result)
    
    empty_points = ()
    try:
        extract_maximum_float(empty_points)
    except EmptyDataError as e:
        print(e)