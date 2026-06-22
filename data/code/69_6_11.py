MILES_TO_FEET_FACTOR = 5280

def convert_miles_to_feet(miles: float) -> float:
    return miles * MILES_TO_FEET_FACTOR

if __name__ == '__main__':
    sample_miles = 10
    result = convert_miles_to_feet(sample_miles)
    print(result)