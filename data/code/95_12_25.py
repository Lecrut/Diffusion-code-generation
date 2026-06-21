def validate_integer(value):
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"Expected integer, got {type(value).__name__}")
    return value

def check_properties(value):
    is_positive = value > 0
    is_even = value % 2 == 0
    is_less_than_100 = value < 100
    return {
        'value': value,
        'is_positive': is_positive,
        'is_even': is_even,
        'is_less_than_100': is_less_than_100
    }

def process_integers(a, b, c):
    validated_values = [validate_integer(a), validate_integer(b), validate_integer(c)]
    results = []
    for val in validated_values:
        results.append(check_properties(val))
    return results

if __name__ == '__main__':
    sample_values = [42, -5, 100]
    output = process_integers(*sample_values)
    print(output)