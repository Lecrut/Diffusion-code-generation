def add_large_integers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    sample_values = {
        'num1': 98765432109876543210,
        'num2': 12345678901234567890
    }
    result = add_large_integers(sample_values['num1'], sample_values['num2'])
    print(result)