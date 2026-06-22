CONVERSION_FACTOR = 5

def validate_kilometers(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Distance must be a number")
    if kilometers < 0:
        raise ValueError("Distance cannot be negative")

def convert_kilometers_to_miles(kilometers):
    validate_kilometers(kilometers)
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kilometers = 20
    miles = convert_kilometers_to_miles(sample_kilometers)
    print(miles)