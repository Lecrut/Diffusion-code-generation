def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def subtract_numbers(a, b):
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 5
    }
    result = subtract_numbers(sample_values['a'], sample_values['b'])
    print(result)