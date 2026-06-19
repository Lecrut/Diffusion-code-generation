def is_significantly_different(a, b, tolerance=1e-10):
    def validate_input(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both inputs must be numbers.")
    
    validate_input(a, b)
    return abs(a - b) > tolerance

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = is_significantly_different(value1, value2)
    print(result)