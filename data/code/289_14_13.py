def nautical_miles_to_kilometers(nautical_miles):
    return round(nautical_miles * 1.852, 2)
if __name__ == '__main__':
    print(nautical_miles_to_kilometers(10))
    print(nautical_miles_to_kilometers(5.5))
    print(nautical_miles_to_kilometers(100.75))