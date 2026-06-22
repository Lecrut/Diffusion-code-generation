def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    sample_x = 5
    sample_y = 3
    result = next(evaluate_condition(sample_x, sample_y))
    print(result)