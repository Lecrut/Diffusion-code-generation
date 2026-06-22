def is_valid_mileage(value):
    return value >= 0

def miles_to_kilometers(miles):
    if not is_valid_mileage(miles):
        raise ValueError("Mileage must be non-negative")
    return miles * 1.60934

if __name__ == '__main__':
    sample_miles = 5
    try:
        kilometers = miles_to_kilometers(sample_miles)
        print(f"{sample_miles} miles is equal to {kilometers:.2f} kilometers")
    except ValueError as e:
        print(e)