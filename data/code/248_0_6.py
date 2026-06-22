def add_two_integers(a, b):
    return a + b

if __name__ == '__main__':
    sample_values = {
        'num1': 10,
        'num2': 25
    }
    result = add_two_integers(sample_values['num1'], sample_values['num2'])
    print(result)