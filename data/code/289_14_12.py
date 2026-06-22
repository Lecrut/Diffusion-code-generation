CONVERSION_FACTOR = 1.852

def nautical_miles_to_kilometers(nautical_miles):
    return round(nautical_miles * CONVERSION_FACTOR, 2)

if __name__ == '__main__':
    print(nautical_miles_to_kilometers(10))
    print(nautical_miles_to_kilometers(5.5))
    print(nautical_miles_to_kilometers(3.75))