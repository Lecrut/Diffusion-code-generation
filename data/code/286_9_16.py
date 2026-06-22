def validate_nautical_miles(nautical_miles):
    if not isinstance(nautical_miles, (int, float)) or nautical_miles < 0:
        raise ValueError("Input must be a non-negative number representing nautical miles")

def nautical_miles_to_kilometers(nautical_miles):
    validate_nautical_miles(nautical_miles)
    return nautical_miles * 1.852

if __name__ == '__main__':
    print(nautical_miles_to_kilometers(0))
    print(nautical_miles_to_kilometers(1))
    print(nautical_miles_to_kilometers(10))
    print(nautical_miles_to_kilometers(100))