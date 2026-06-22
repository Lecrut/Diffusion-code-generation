MILES_TO_FEET_FACTOR = 5280

def convert_distance(mile_values):
    conversion_factor = MILES_TO_FEET_FACTOR
    feet_values = [mile * conversion_factor for mile in mile_values]
    return feet_values

if __name__ == '__main__':
    sample_input = [0.5, 3.0, 7.25, 12]
    output_feet = convert_distance(sample_input)
    print(output_feet)