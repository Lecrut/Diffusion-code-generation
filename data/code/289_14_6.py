conversion_factor = {'nautical_miles': 1.852}

def nautical_miles_to_kilometers(nautical_miles):
    if not isinstance(nautical_miles, (int, float)):
        raise ValueError("Input must be an integer or floating-point number")
    return round(nautical_miles * conversion_factor['nautical_miles'], 2)

if __name__ == '__main__':
    print(nautical_miles_to_kilometers(10))
    print(nautical_miles_to_kilometers(5.5))
    print(nautical_miles_to_kilometers(3.75))