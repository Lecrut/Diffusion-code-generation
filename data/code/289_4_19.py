def validate_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")

def nautical_miles_to_kilometers(nautical_miles):
    return round(nautical_miles * 1.852, 2)

if __name__ == '__main__':
    sample_value = 10
    validate_input(sample_value)
    result = nautical_miles_to_kilometers(sample_value)
    print(result)