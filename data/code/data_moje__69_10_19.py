def miles_to_feet(miles):
    return miles * 5280.0

if __name__ == '__main__':
    test_miles = 2.5
    result = miles_to_feet(test_miles)
    print(result)