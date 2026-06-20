def validate_inputs(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return x, y

def check_condition(x, y):
    x, y = validate_inputs(x, y)
    return x and y

if __name__ == '__main__':
    print(check_condition(5, 3))
    print(check_condition(10, 10))
    print(check_condition(2, 7))
    print(check_condition(0, -5))