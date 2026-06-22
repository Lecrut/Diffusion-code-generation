def validate_large_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return True

def sum_large_integers(a, b):
    if not validate_large_integers(a, b):
        return None
    return a + b

if __name__ == '__main__':
    sample_values = {
        'a': 12345678901234567890,
        'b': 98765432109876543210
    }
    result = sum_large_integers(sample_values['a'], sample_values['b'])
    print(result)