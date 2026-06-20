def multiply_values(num1, num2):
    return num1 * num2

if __name__ == '__main__':
    sample_values = {
        'value1': 5,
        'value2': 10
    }
    result = multiply_values(sample_values['value1'], sample_values['value2'])
    print(result)