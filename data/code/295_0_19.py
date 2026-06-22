def validate_input(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Input must be a non-negative number")

def meters_to_kilometers(meters):
    validate_input(meters)
    return round(meters / 1000.0, 2)

if __name__ == '__main__':
    sample_meters = 5000
    kilometers = meters_to_kilometers(sample_meters)
    print(f"{sample_meters} meters is equal to {kilometers} kilometers")