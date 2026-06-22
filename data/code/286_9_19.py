def nautical_miles_to_kilometers(nautical_miles):
    if nautical_miles == 0:
        return 0
    conversion_factor = 1.852
    return nautical_miles * conversion_factor

if __name__ == '__main__':
    print(nautical_miles_to_kilometers(0))
    print(nautical_miles_to_kilometers(1))
    print(nautical_miles_to_kilometers(10))
    print(nautical_miles_to_kilometers(100))