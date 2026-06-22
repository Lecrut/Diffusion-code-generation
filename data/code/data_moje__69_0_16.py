def miles_to_feet(miles):
    feet_per_mile = 5280
    return miles * feet_per_mile
if __name__ == '__main__':
    sample_miles = 10.5
    result = miles_to_feet(sample_miles)
    print(result)