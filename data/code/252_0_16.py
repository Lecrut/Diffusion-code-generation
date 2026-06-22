def compare_two_simple_quantities_now_transform(a, b):
    return a > b

if __name__ == '__main__':
    sample_values = {
        'a': 5,
        'b': 3
    }
    result = compare_two_simple_quantities_now_transform(sample_values['a'], sample_values['b'])
    print(result)