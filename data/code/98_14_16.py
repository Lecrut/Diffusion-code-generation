def validate_condition_x(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be numeric")
    return value > 0

def validate_condition_y(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be numeric")
    return value < 10

def validate_condition_z(value):
    if not isinstance(value, str):
        raise ValueError("Value must be string")
    return len(value) > 0

def evaluate_conditions(x_val, y_val, z_val, w_val):
    cond_x = validate_condition_x(x_val)
    cond_y = validate_condition_y(y_val)
    cond_z = validate_condition_z(z_val)
    cond_w = w_val is not None
    
    return (cond_x and cond_y) or (cond_z and cond_w)

if __name__ == '__main__':
    val_x = 15
    val_y = 2
    val_z = "hello"
    val_w = True
    result = evaluate_conditions(val_x, val_y, val_z, val_w)
    print(result)