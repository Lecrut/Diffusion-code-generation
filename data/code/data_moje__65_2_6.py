def _validate_positive(value):
    if value < 0:
        raise ValueError("Input must be non-negative")
    return value

def feet_to_inches(feet):
    feet = _validate_positive(feet)
    return feet * 12

if __name__ == '__main__':
    sample_feet = 10
    result = feet_to_inches(sample_feet)
    print(result)