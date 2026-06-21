def check_difference(a, b):
    return not (a == b)

if __name__ == '__main__':
    sample_values = {'value1': 42, 'value2': 43}
    result = check_difference(sample_values['value1'], sample_values['value2'])
    print(result)