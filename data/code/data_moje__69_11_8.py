MILES_TO_FEET_FACTOR = 5280

def convert_distance(miles):
    return [miles * MILES_TO_FEET_FACTOR for miles in miles]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10]
    result = convert_distance(sample_miles)
    print(result)