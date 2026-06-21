KILOMETERS_TO_MILES_CONVERSION_FACTOR = 5

def convert_kilometers_to_miles(kilometers):
    return kilometers * KILOMETERS_TO_MILES_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kilometers = 20
    miles = convert_kilometers_to_miles(sample_kilometers)
    print(miles)