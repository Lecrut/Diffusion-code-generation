def validate_numbers(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both arguments must be numbers.")
    
    return a, b

def add_numbers(a, b):
    valid_a, valid_b = validate_numbers(a, b)
    return valid_a + valid_b

if __name__ == '__main__':
    result = add_numbers(4.5, 3)
    print(result)