conversion_factor = {"miles_to_kilometers": 1.60934}

def convert_miles_to_kilometers(miles):
    return miles * conversion_factor["miles_to_kilometers"]

if __name__ == '__main__':
    sample_miles = 5
    result_km = convert_miles_to_kilometers(sample_miles)
    print(result_km)