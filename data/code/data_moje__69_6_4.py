MILES_TO_FEET_FACTOR = 5280

def miles_to_feet(miles):
    return miles * MILES_TO_FEET_FACTOR

if __name__ == '__main__':
    sample_miles = 1
    result = miles_to_feet(sample_miles)
    print(result)