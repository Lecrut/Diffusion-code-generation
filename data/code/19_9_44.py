def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    sample_values = [(10, 5), (3, 7), (8, 8)]
    for x, y in sample_values:
        result = list(evaluate_condition(x, y))
        print(result[0])