MILES_TO_FEET_FACTOR = 5280

def convert_distance(miles):
    return [mile * MILES_TO_FEET_FACTOR for mile in miles]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10, 0.5]
    feet_values = convert_distance(sample_miles)
    print(feet_values)