def evaluate_condition(x, y):
    def validate_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both x and y must be numbers.")
    
    validate_numbers(x, y)
    yield x > y

if __name__ == '__main__':
    sample_x = 7
    sample_y = 3
    result_generator = evaluate_condition(sample_x, sample_y)
    try:
        result = next(result_generator)
        print(result)
    except ValueError as e:
        print(e)