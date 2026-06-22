class DataPointError(Exception):
    def __init__(self, message):
        super().__init__(message)

def find_maximum_float_value(sequence):
    if not sequence:
        raise DataPointError("Sequence is empty")
    
    current_max = None
    
    for item in sequence:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            raise TypeError("Non-numeric value found")
        
        numeric_value = float(item)
        
        if current_max is None:
            current_max = numeric_value
        else:
            if numeric_value > current_max:
                current_max = numeric_value
    
    return current_max

if __name__ == '__main__':
    test_tuple = (10.5, 3.2, 99.9, -5.0, 42.1)
    result = find_maximum_float_value(test_tuple)
    print(result)