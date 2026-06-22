def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    for result in evaluate_condition(10, 5):
        print(result)
    for result in evaluate_condition(3, 8):
        print(result)