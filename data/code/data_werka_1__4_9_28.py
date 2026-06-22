def convert_distance(distance, conversion_factor):
    return distance * conversion_factor
if __name__ == '__main__':
    miles_to_kilometers = 1.60934
    kilometers_to_miles = 0.621371
    sample_miles = 5
    sample_kilometers = 10
    converted_km = convert_distance(sample_miles, miles_to_kilometers)
    print(f'{sample_miles} miles is {converted_km:.2f} kilometers')
    converted_mi = convert_distance(sample_kilometers, kilometers_to_miles)
    print(f'{sample_kilometers} kilometers is {converted_mi:.2f} miles')