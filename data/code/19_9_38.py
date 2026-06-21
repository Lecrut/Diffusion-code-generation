def validate_numbers(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers")

def evaluate_condition(x, y):
    validate_numbers(x, y)
    yield x > y

if __name__ == '__main__':
    sample_x = 25
    sample_y = 15
    result_generator = evaluate_condition(sample_x, sample_y)
    result = next(result_generator)
    print(result)