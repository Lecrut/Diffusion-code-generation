def validate_three_values(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise ValueError("Inputs must be numeric")
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("Inputs must be integers")
    
    threshold = 100
    min_val = 0
    
    for val in (a, b, c):
        if val <= min_val:
            return False
        if val >= threshold:
            return False
        if val % 2 != 0:
            return False
            
    return True

if __name__ == '__main__':
    result = validate_three_values(2, 4, 6)
    print(result)
    
    result_false = validate_three_values(1, 4, 6)
    print(result_false)
    
    result_large = validate_three_values(2, 4, 102)
    print(result_large)
    
    result_neg = validate_three_values(-2, 4, 6)
    print(result_neg)