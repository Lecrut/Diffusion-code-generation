def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    test_x = 50
    test_y = 25
    condition_generator = evaluate_condition(test_x, test_y)
    is_greater = next(condition_generator)
    print(is_greater)