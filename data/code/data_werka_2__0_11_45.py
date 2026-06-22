def validate_kilometers(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Distance must be a number")
    if kilometers < 0:
        raise ValueError("Distance cannot be negative")

def kilometers_to_miles(kilometers):
    validate_kilometers(kilometers)
    conversion_factor = 5
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = 20
    miles = kilometers_to_miles(sample_kilometers)
    print(miles)