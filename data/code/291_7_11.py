def compare_miles_to_km(miles):
    km = miles * 1.60934
    return km

if __name__ == '__main__':
    sample_miles = 5
    result_km = compare_miles_to_km(sample_miles)
    print(result_km)