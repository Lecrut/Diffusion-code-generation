def check_difference(a, b):
    def validate_inputs(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both inputs must be integers or floats.")
    
    validate_inputs(a, b)
    return a != b

if __name__ == '__main__':
    sample_value1 = 42.0
    sample_value2 = 43
    result = check_difference(sample_value1, sample_value2)
    print(result)