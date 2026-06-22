def miles_to_kilometers(miles):
    if miles <= 0:
        return 0
    conversion_factor = 1.60934
    kilometers = miles * conversion_factor
    return kilometers

if __name__ == '__main__':
    sample_miles = 5
    result = miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {result:.2f} kilometers")