import operator

def multiply(a, b):
    return operator.mul(a, b)

if __name__ == '__main__':
    sample_values = {
        'num1': 8,
        'num2': 3
    }
    result = multiply(sample_values['num1'], sample_values['num2'])
    print(result)