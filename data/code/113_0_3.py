def subtract_amounts(num1, num2):
    return num1 - num2

if __name__ == '__main__':
    sample_values = {
        'num1': 15,
        'num2': 7
    }
    
    result = subtract_amounts(sample_values['num1'], sample_values['num2'])
    print(result)