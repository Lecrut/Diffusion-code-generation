def multiply_figures(a: float, b: float) -> float:
    return a * b

if __name__ == '__main__':
    sample_values = {
        'num1': 7.5,
        'num2': 8.0
    }
    result = multiply_figures(sample_values['num1'], sample_values['num2'])
    print(result)