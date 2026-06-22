def check_difference(a, b):
    def validate_inputs(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both inputs must be numerical values.")
    
    validate_inputs(a, b)
    return a != b

if __name__ == '__main__':
    value1 = 3.14
    value2 = 2.71
    result = check_difference(value1, value2)
    print(result)