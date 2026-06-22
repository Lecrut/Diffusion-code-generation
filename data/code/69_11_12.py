MILES_TO_FEET_FACTOR = 5280

def convert_distance(mile_values):
    if not mile_values:
        return []
    return [value * MILES_TO_FEET_FACTOR for value in mile_values]

if __name__ == '__main__':
    miles_input = [0.5, 1, 5, 10]
    output_feet = convert_distance(miles_input)
    print(output_feet)