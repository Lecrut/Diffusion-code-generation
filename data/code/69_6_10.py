MILES_TO_FEET = 5280

def miles_to_feet(miles):
    return miles * MILES_TO_FEET

if __name__ == '__main__':
    sample_miles = 10
    result = miles_to_feet(sample_miles)
    print(result)