def evaluate_or_condition(a, b):
    return (a > 5) or (b < 10)

if __name__ == '__main__':
    sample_data = {
        'a': 6,
        'b': 9
    }
    result = evaluate_or_condition(sample_data['a'], sample_data['b'])
    print(result)