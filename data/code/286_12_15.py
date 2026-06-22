def miles_to_kilometers(miles):
    conversion_factor = 1.60934
    kilometers = miles * conversion_factor
    return kilometers

if __name__ == '__main__':
    sample_miles = 5
    result_km = miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {result_km:.2f} kilometers")