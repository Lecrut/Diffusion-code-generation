def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 5
    }
    result = subtract_numbers(sample_values['a'], sample_values['b'])
    print(result)