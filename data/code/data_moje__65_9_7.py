def validate_positive(value):
    if value < 0:
        raise ValueError("Length must be non-negative")
    return True

def convert_feet_to_inches(feet):
    validate_positive(feet)
    return feet * 12

if __name__ == '__main__':
    sample_feet = 10
    result = convert_feet_to_inches(sample_feet)
    print(result)