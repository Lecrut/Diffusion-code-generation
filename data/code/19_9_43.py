def evaluate_condition(x, y):
    condition_map = {
        'x_greater_than_y': x > y
    }
    yield condition_map['x_greater_than_y']

if __name__ == '__main__':
    sample_x = 15
    sample_y = 25
    result_generator = evaluate_condition(sample_x, sample_y)
    result = next(result_generator)
    print(result)