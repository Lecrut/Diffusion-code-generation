def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        return result

if __name__ == '__main__':
    sample_values = {
        'num1': 10,
        'num2': 0
    }
    result = divide_numbers(sample_values['num1'], sample_values['num2'])
    print(result)