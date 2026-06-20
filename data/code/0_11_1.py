METERS_TO_FEET = 3.28084

def convert_meters_to_feet(meters):
    return meters * METERS_TO_FEET

if __name__ == '__main__':
    length_in_meters = 10
    length_in_feet = convert_meters_to_feet(length_in_meters)
    print(length_in_feet)