def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

if __name__ == '__main__':
    sample_kilometers = 5.0
    sample_miles = 5.0
    result_km_to_miles = kilometers_to_miles(sample_kilometers)
    result_miles_to_km = miles_to_kilometers(sample_miles)
    print(f"{sample_kilometers} kilometers is {result_km_to_miles} miles")
    print(f"{sample_miles} miles is {result_miles_to_km} kilometers")