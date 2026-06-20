def validate_inputs(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers")
    if x <= 5:
        raise ValueError("x must be greater than 5")
    if y >= 10:
        raise ValueError("y must be less than 10")

def check_combined_conditions(x, y):
    validate_inputs(x, y)
    return x > 5 and y < 10

if __name__ == '__main__':
    try:
        result = check_combined_conditions(6, 8)
        print(result)
    except ValueError as e:
        print(e)