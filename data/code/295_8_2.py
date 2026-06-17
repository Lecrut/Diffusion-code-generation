import sys
def convert_miles_to_km(miles):
    kilometers = miles * 1.60934
    return kilometers
if __name__ == '__main__':
    sample_miles = 100
    result_km = convert_miles_to_km(sample_miles)
    print(result_km)