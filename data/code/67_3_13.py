def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    sample_values = {
        'num1': 7,
        'num2': 3
    }
    result = next(sum_generator(sample_values['num1'], sample_values['num2']))
    print(result)