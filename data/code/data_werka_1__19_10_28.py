def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    x = 10
    y = 5
    result = list(evaluate_condition(x, y))
    print(result[0])