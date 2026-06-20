def add_two_numbers(a: float, b: float) -> float:
    return a + b

if __name__ == '__main__':
    sample_values = {
        'num1': 5.0,
        'num2': 3.0
    }
    result = add_two_numbers(sample_values['num1'], sample_values['num2'])
    print(result)