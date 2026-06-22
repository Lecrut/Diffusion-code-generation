def evaluate_boolean_matrix(x, y, z):
    status_map = {
        "high_x_low_y": "X is high and Y is low",
        "zero_z": "Z is zero",
        "negative_sum": "Sum is negative",
        "default": "None matched"
    }
    conditions = {
        "high_x_low_y": x > 50 and y < 10,
        "zero_z": z == 0,
        "negative_sum": x + y + z < 0
    }
    for key, is_met in conditions.items():
        if is_met:
            return status_map[key]
    return status_map["default"]

if __name__ == '__main__':
    val_x = 60
    val_y = 5
    val_z = -100
    res = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(res)
    val_x = 10
    val_y = 20
    val_z = 0
    res = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(res)
    val_x = -10
    val_y = -20
    val_z = -30
    res = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(res)
    val_x = 1
    val_y = 1
    val_z = 1
    res = evaluate_boolean_matrix(val_x, val_y, val_z)
    print(res)