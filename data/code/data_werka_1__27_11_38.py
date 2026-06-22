def is_different(a, b):
    def validate_inputs(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both inputs must be integers or floats.")
    
    validate_inputs(a, b)
    return a != b

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = is_different(value1, value2)
    print(result)