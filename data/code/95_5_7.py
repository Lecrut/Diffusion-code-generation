def evaluate_conditions(x, y, z):
    is_x_positive = x > 0
    is_y_even = y % 2 == 0
    is_z_divisible_by_x = z % x == 0
    return (is_x_positive, is_y_even, is_z_divisible_by_x)

if __name__ == '__main__':
    sample_values = (13, 8, 26)
    result = evaluate_conditions(*sample_values)
    print(result)