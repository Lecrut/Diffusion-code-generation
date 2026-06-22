MILES_TO_FEET_FACTOR = 5280

def convert_distance(miles):
    return [m * MILES_TO_FEET_FACTOR for m in miles]

if __name__ == '__main__':
    sample_miles = [1.0, 2.5, 3.75]
    result = convert_distance(sample_miles)
    print(result)