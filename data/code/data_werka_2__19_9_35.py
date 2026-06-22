def evaluate_condition(x, y):
    condition = x > y
    yield condition

if __name__ == '__main__':
    sample_x = 20
    sample_y = 30
    result_generator = evaluate_condition(sample_x, sample_y)
    result = next(result_generator)
    print(result)