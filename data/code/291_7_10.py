CONVERSION_FACTOR = 1.60934

def miles_to_kilometers(miles):
    return miles * CONVERSION_FACTOR

def kilometers_to_miles(kilometers):
    return kilometers / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_miles = 5
    sample_kilometers = 8.04672
    
    print(f"{sample_miles} miles is {miles_to_kilometers(sample_miles)} kilometers")
    print(f"{sample_kilometers} kilometers is {kilometers_to_miles(sample_kilometers)} miles")