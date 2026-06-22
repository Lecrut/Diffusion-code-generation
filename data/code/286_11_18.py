CONVERSION_FACTOR = 0.3048

def convert_feet_to_meters(feet):
    return feet * CONVERSION_FACTOR

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = convert_feet_to_meters(length_feet)
    print(f"10.0 ft converted to meters: {result_meters}")