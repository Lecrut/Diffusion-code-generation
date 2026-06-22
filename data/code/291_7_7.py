def compare_miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

if __name__ == '__main__':
    sample_miles = 5
    result_km = compare_miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {result_km:.2f} kilometers")