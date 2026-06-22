def validate_inputs(x, y, z):
    if not isinstance(x, (int, float)):
        raise ValueError("x must be numeric")
    if not isinstance(y, (int, float)):
        raise ValueError("y must be numeric")
    if not isinstance(z, (int, float)):
        raise ValueError("z must be numeric")
    return True

def evaluate_logic(x, y, z):
    validate_inputs(x, y, z)
    
    if x > 0 and y > 0:
        status = "positive_pair"
    elif x < 0 and y < 0:
        status = "negative_pair"
    elif z == 0:
        status = "zero_z"
    elif x + y == z:
        status = "sum_match"
    else:
        status = "default_case"
        
    return status

if __name__ == '__main__':
    val_x = 5
    val_y = 3
    val_z = 8
    result = evaluate_logic(val_x, val_y, val_z)
    print(result)
    
    val_x = -2
    val_y = -4
    val_z = 0
    result = evaluate_logic(val_x, val_y, val_z)
    print(result)