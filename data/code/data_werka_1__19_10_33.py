def evaluate_condition(x, y):
    yield (x > y)
if __name__ == '__main__':
    x = 10
    y = 5
    condition_result = next(evaluate_condition(x, y))
    print(condition_result)