def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    sample_x = 10
    sample_y = 5
    result = next(evaluate_condition(sample_x, sample_y))
    print(result)