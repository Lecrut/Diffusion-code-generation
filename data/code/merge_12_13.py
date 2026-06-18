def calculate_sequence(x, y, z):
    sum_xy = x + y
    result = sum_xy - z
    return result
if __name__ == '__main__':
    x_val = 10
    y_val = 5
    z_val = 3
    output = calculate_sequence(x_val, y_val, z_val)
    print(output)