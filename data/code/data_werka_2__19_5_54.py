def validate_input(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers")

if __name__ == '__main__':
    x = 13
    y = 47
    validate_input(x, y)
    result = (x > 10) and (y < 50)
    print(result)