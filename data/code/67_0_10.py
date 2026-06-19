def sum_two_numbers(a, b):
    return a + b

if __name__ == '__main__':
    values = {
        'number1': 25,
        'number2': 30
    }
    result = sum_two_numbers(values['number1'], values['number2'])
    print(result)