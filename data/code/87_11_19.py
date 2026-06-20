def validate_inputs(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Inputs must be numbers")
    if x <= 5:
        raise ValueError("x must be greater than 5")
    if y >= 10:
        raise ValueError("y must be less than 10")

def check_combined_conditions(x, y):
    validate_inputs(x, y)
    return x > 5 and y < 10

if __name__ == '__main__':
    sample_x = 6
    sample_y = 8
    result = check_combined_conditions(sample_x, sample_y)
    print(result)