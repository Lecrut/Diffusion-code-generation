def evaluate_boolean_matrix(x, y, z):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
        raise ValueError("Inputs must be numeric")
    if x < 0 or y < 0 or z < 0:
        raise ValueError("Inputs must be non-negative")
    if x > 100 or y > 100 or z > 100:
        raise ValueError("Inputs must be less than or equal to 100")
    if x > 50 and y > 50:
        status = "High High"
    elif x > 50 and z > 50:
        status = "High Z"
    elif y > 50 and z > 50:
        status = "High YZ"
    elif x == 0 and y == 0 and z == 0:
        status = "Zero State"
    else:
        status = "Mixed State"
    return status

if __name__ == '__main__':
    val_x = 60
    val_y = 70
    val_z = 20
    result = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(result)
    val_x = 10
    val_y = 10
    val_z = 10
    result = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(result)
    val_x = 0
    val_y = 0
    val_z = 0
    result = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(result)