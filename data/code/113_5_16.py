def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an integer or float")

def subtract_numbers(a, b):
    validate_number(a)
    validate_number(b)
    return a - b

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 5
    }
    result = subtract_numbers(sample_values['a'], sample_values['b'])
    print(result)