def convert_miles_to_kilometers(miles):
    conversion_factor = 1.60934
    return miles * conversion_factor

if __name__ == '__main__':
    sample_miles = 5
    result_km = convert_miles_to_kilometers(sample_miles)
    print(result_km)