def miles_to_kilometers(miles):
    conversion_factor = 1.60934
    return miles * conversion_factor

if __name__ == '__main__':
    sample_miles = 5
    kilometers = miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {kilometers:.2f} kilometers")