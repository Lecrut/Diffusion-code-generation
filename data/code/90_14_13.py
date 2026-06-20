def is_greater_than_ten(num1, num2):
    return num1 > 10 or num2 > 10

if __name__ == '__main__':
    sample_values = {
        'num1': 5,
        'num2': 15
    }
    result = is_greater_than_ten(sample_values['num1'], sample_values['num2'])
    print(result)