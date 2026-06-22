MILES_TO_FEET_FACTOR = 5280.0

def miles_to_feet(miles):
    return miles * MILES_TO_FEET_FACTOR

if __name__ == '__main__':
    result = miles_to_feet(2)
    print(result)