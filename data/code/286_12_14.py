CONVERSION_FACTOR = 1.60934

def miles_to_kilometers(miles):
    return miles * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = 5
    kilometers = miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {kilometers:.2f} kilometers")