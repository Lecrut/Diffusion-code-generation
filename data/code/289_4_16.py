def nautical_miles_to_kilometers(nautical_miles):
    return round(nautical_miles * 1.852, 2)

if __name__ == '__main__':
    print(nautical_miles_to_kilometers(1))
    print(nautical_miles_to_kilometers(5))
    print(nautical_miles_to_kilometers(10))