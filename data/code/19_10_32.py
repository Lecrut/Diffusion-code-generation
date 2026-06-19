def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    gen = evaluate_condition(10, 5)
    print(next(gen))