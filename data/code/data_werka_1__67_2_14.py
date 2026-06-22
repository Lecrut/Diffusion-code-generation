def add_floats(a, b):
    return a + b

if __name__ == '__main__':
    sample_values = {
        'value1': 0.1,
        'value2': 0.2
    }
    result = add_floats(sample_values['value1'], sample_values['value2'])
    print(result)