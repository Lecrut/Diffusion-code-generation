def convert_miles_to_kilometers(miles):
    return miles * 1.60934

if __name__ == '__main__':
    sample_miles = 5
    kilometers = convert_miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {kilometers:.2f} kilometers")