MILES_TO_FEET_FACTOR = 5280

def convert_distance(mile_values):
    return [miles * MILES_TO_FEET_FACTOR for miles in mile_values]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10, 0.5]
    feet_values = convert_distance(sample_miles)
    print(feet_values)