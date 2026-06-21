def evaluate_condition(x, y):
    condition = x > y
    yield condition

if __name__ == '__main__':
    sample_x = 50
    sample_y = 25
    result_generator = evaluate_condition(sample_x, sample_y)
    for result in result_generator:
        print(result)