MILES_TO_FEET_FACTOR = 5280

def convert_distance(miles_list):
    return [miles * MILES_TO_FEET_FACTOR for miles in miles_list]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10]
    result = convert_distance(sample_miles)
    print(result)