METERS_TO_FEET_CONVERSION_FACTOR = 3.28084

def convert_meters_to_feet(meters: float) -> float:
    return meters * METERS_TO_FEET_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_value = 10
    result = convert_meters_to_feet(sample_value)
    print(result)