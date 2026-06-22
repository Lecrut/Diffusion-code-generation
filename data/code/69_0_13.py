def miles_to_feet(miles):
    return miles * 5280.0

if __name__ == '__main__':
    sample_miles = 3.5
    result = miles_to_feet(sample_miles)
    print(result)
    print(miles_to_feet(1.0))
    print(miles_to_feet(0.125))