def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Both arguments must be integers.")

def sum_large_integers(a, b):
    validate_integer(a)
    validate_integer(b)
    return a + b

if __name__ == '__main__':
    sample_values = {
        'a': 12345678901234567890,
        'b': 98765432109876543210
    }
    result = sum_large_integers(sample_values['a'], sample_values['b'])
    print(result)