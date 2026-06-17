def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers
if __name__ == '__main__':
    sample_miles = 100
    sample_kilometers = miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {sample_kilometers} kilometers")