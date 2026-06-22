def validate_nautical_miles_to_km(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be numeric.")

def nautical_miles_to_km(nautical_miles):
    validate_nautical_miles_to_km(nautical_miles)
    kilometers = nautical_miles * 1.852
    return round(kilometers, 2)

if __name__ == '__main__':
    sample_value = 10
    print(f"{sample_value} nautical miles is {nautical_miles_to_km(sample_value)} km")