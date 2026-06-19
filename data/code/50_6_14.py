def non_negative_difference(x, y):
    return abs(y - x)

if __name__ == '__main__':
    sample_values = {'a': 10, 'b': 5}
    result = non_negative_difference(sample_values['a'], sample_values['b'])
    print(result)