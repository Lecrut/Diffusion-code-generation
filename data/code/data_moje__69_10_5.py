def miles_to_feet(miles):
    return miles * 5280.0

if __name__ == '__main__':
    sample_miles = 2.5
    result = miles_to_feet(sample_miles)
    print(result)
    sample_miles_2 = 0.125
    result_2 = miles_to_feet(sample_miles_2)
    print(result_2)