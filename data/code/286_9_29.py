conversion_factor = 1.852

def validate_nautical_miles(nautical_miles):
    if not isinstance(nautical_miles, (int, float)) or nautical_miles < 0:
        raise ValueError("Input must be a non-negative number")

def nautical_miles_to_kilometers(nautical_miles):
    validate_nautical_miles(nautical_miles)
    return nautical_miles * conversion_factor

if __name__ == '__main__':
    print(f"0 nautical miles is {nautical_miles_to_kilometers(0)} kilometers")
    print(f"1 nautical mile is {nautical_miles_to_kilometers(1)} kilometers")
    print(f"50 nautical miles is {nautical_miles_to_kilometers(50)} kilometers")