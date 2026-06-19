def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    for result in evaluate_condition(5, 3):
        print(result)