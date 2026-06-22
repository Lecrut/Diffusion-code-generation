CONVERSION_FACTOR = 1.852

def nautical_miles_to_kilometers(nautical_miles):
    if nautical_miles == 0:
        return 0
    return nautical_miles * CONVERSION_FACTOR

if __name__ == '__main__':
    print(nautical_miles_to_kilometers(0))
    print(nautical_miles_to_kilometers(1))
    print(nautical_miles_to_kilometers(5))
    print(nautical_miles_to_kilometers(20))