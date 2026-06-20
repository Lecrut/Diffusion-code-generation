METERS_TO_FEET_CONVERSION_FACTOR = 3.28084

def convert_meters_to_feet(length_in_meters: float) -> float:
    return length_in_meters * METERS_TO_FEET_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_meters = 10.0
    result_feet = convert_meters_to_feet(sample_meters)
    print(result_feet)