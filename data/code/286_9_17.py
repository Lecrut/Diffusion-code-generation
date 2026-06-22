def nautical_miles_to_kilometers(nautical_miles):
    if nautical_miles == 0:
        return 0
    else:
        return nautical_miles * 1.852
if __name__ == '__main__':
    print(nautical_miles_to_kilometers(0))
    print(nautical_miles_to_kilometers(1))
    print(nautical_miles_to_kilometers(10))