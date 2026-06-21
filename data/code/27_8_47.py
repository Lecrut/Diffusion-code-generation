def check_difference(a, b):
    return not (a == b)

if __name__ == '__main__':
    sample_values = {
        'first': 42,
        'second': 43
    }
    result = check_difference(sample_values['first'], sample_values['second'])
    print(result)