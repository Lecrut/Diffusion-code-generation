MILES_TO_FEET = 5280

def convert_miles_to_feet(miles):
    return miles * MILES_TO_FEET

if __name__ == '__main__':
    miles_input = 10
    feet_output = convert_miles_to_feet(miles_input)
    print(feet_output)