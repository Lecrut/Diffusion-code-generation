def add_decimals(a, b):
    return round(a + b, 2)

if __name__ == '__main__':
    sample_values = {'a': 3.5, 'b': 2.7}
    result = add_decimals(sample_values['a'], sample_values['b'])
    print(result)