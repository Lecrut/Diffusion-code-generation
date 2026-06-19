def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    x = 5
    y = 3
    result = next(evaluate_condition(x, y))
    print(result)