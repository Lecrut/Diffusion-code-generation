def evaluate_condition(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers")
    yield x > y

if __name__ == '__main__':
    sample_x = 15
    sample_y = 25
    try:
        result = next(evaluate_condition(sample_x, sample_y))
        print(result)
    except ValueError as e:
        print(e)