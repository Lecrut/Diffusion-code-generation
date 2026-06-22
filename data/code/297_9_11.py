MILE_TO_KILOMETRE = 1.60934

def convert_miles_to_kilometres(miles):
    return miles * MILE_TO_KILOMETRE

if __name__ == '__main__':
    sample_miles = 5
    result_km = convert_miles_to_kilometres(sample_miles)
    print(result_km)