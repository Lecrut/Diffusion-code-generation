def validate_condition_a(value):
    return value is not None and isinstance(value, (int, float))

def validate_condition_b(value):
    return value is not None and isinstance(value, (int, float))

def validate_condition_c(value):
    return value is not None and isinstance(value, (int, float))

def validate_condition_d(value):
    return value is not None and isinstance(value, (int, float))

def evaluate_conditions(a, b, c, d):
    a_valid = validate_condition_a(a)
    b_valid = validate_condition_b(b)
    c_valid = validate_condition_c(c)
    d_valid = validate_condition_d(d)
    
    if not (a_valid and b_valid and c_valid and d_valid):
        raise ValueError("All inputs must be valid numbers")
    
    cond_a = a > 0
    cond_b = b < 10
    cond_c = c == d
    
    result = (cond_a and cond_b) or cond_c
    return bool(result)

if __name__ == '__main__':
    val_a = 5
    val_b = 2
    val_c = 15
    val_d = 15
    print(evaluate_conditions(val_a, val_b, val_c, val_d))