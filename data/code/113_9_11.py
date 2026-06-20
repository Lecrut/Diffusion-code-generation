def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    sample_values = {
        'num1': 123456789012345678901234567890,
        'num2': 987654321098765432109876543210
    }
    result = subtract_numbers(sample_values['num1'], sample_values['num2'])
    print(result)