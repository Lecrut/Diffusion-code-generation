CONVERSION_FACTOR = 1.60934

def compare_lengths(miles, kilometers):
    miles_in_km = miles * CONVERSION_FACTOR
    return miles_in_km == kilometers

if __name__ == '__main__':
    sample_miles = 5
    sample_kilometers = 8.04672
    result = compare_lengths(sample_miles, sample_kilometers)
    print(result)