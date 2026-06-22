MILES_TO_FEET_FACTOR = 5280

def miles_to_feet(miles, factor=MILES_TO_FEET_FACTOR):
    return miles * factor

if __name__ == '__main__':
    sample_miles = 10
    result = miles_to_feet(sample_miles)
    print(result)