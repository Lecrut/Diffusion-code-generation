def check_difference(a, b):
    return not (a == b)

if __name__ == '__main__':
    sample_values = {
        'first_value': 10,
        'second_value': 20
    }
    result = check_difference(sample_values['first_value'], sample_values['second_value'])
    print(result)