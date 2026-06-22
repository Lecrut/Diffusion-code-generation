def miles_to_feet(miles):
    return miles * 5280.0

if __name__ == '__main__':
    sample_miles_1 = 1.0
    sample_miles_2 = 10.5
    sample_miles_3 = 0.001
    print(miles_to_feet(sample_miles_1))
    print(miles_to_feet(sample_miles_2))
    print(miles_to_feet(sample_miles_3))