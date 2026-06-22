def miles_to_feet(miles):
    feet_per_mile = 5280
    return miles * feet_per_mile
if __name__ == '__main__':
    sample_miles = 1.0
    print(miles_to_feet(sample_miles))
    sample_miles_2 = 0.5
    print(miles_to_feet(sample_miles_2))
    sample_miles_3 = 10.123
    print(miles_to_feet(sample_miles_3))