def validate_and_evaluate(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers")
    return (x > 10) and (y < 50)

if __name__ == '__main__':
    x = 13
    y = 47
    result = validate_and_evaluate(x, y)
    print(result)