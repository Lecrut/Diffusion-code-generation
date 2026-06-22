def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    SAMPLE_X = 15
    SAMPLE_Y = 25
    result_iterator = evaluate_condition(SAMPLE_X, SAMPLE_Y)
    condition_result = next(result_iterator)
    print(condition_result)