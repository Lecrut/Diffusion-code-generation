def evaluate_conditions(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise ValueError("Inputs must be numeric")
    
    if a <= 0:
        return False
    
    if b % 2 != 0:
        return False
    
    product = a * b
    if product == 0:
        return False
        
    return c % product == 0

if __name__ == '__main__':
    a_val = 2
    b_val = 4
    c_val = 8
    result = evaluate_conditions(a_val, b_val, c_val)
    print(result)