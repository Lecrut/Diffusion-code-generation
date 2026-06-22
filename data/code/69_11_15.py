MILES_TO_FEET_FACTOR = 5280

def convert_distance(miles):
    return [miles_value * MILES_TO_FEET_FACTOR for miles_value in miles]

if __name__ == '__main__':
    result = convert_distance([1.0, 2.5, 10])
    print(result)