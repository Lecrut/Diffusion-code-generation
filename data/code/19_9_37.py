def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    sample_x = 25
    sample_y = 10
    result_generator = evaluate_condition(sample_x, sample_y)
    result = next(result_generator)
    print(result)