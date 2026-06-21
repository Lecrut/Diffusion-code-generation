def evaluate_condition(x, y):
    yield x > y

if __name__ == '__main__':
    sample_values = {
        'x': 15,
        'y': 8
    }
    result = next(evaluate_condition(sample_values['x'], sample_values['y']))
    print(result)