def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

def miles_to_kilometers(miles):
    validate_input(miles)
    return miles * 1.60934

if __name__ == '__main__':
    sample_value = 5
    print(miles_to_kilometers(sample_value))