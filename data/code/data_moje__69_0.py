def miles_to_feet(miles):
    conversion_factor = 5280.0
    return miles * conversion_factor

if __name__ == '__main__':
    sample_miles_1 = 1.0
    sample_miles_2 = 2.5
    sample_miles_3 = 0.001
    result_1 = miles_to_feet(sample_miles_1)
    result_2 = miles_to_feet(sample_miles_2)
    result_3 = miles_to_feet(sample_miles_3)
    print(result_1)
    print(result_2)
    print(result_3)