class DataPointError(Exception):
    def __init__(self, message="Invalid data point sequence."):
        super().__init__(message)

def _validate_and_convert(value):
    if isinstance(value, bool):
        raise TypeError("Boolean values are not allowed.")
    if not isinstance(value, (int, float)):
        raise TypeError("All values must be numeric.")
    return float(value)

def get_max_from_tuple(data_tuple):
    if not data_tuple:
        raise DataPointError("The provided tuple is empty.")
    
    current_max = None
    
    for item in data_tuple:
        numeric_item = _validate_and_convert(item)
        
        if current_max is None:
            current_max = numeric_item
        elif numeric_item > current_max:
            current_max = numeric_item
            
    return current_max

if __name__ == '__main__':
    test_values = (1.5, 2.3, 0.9, 4.7, 3.1)
    result_value = get_max_from_tuple(test_values)
    print(result_value)