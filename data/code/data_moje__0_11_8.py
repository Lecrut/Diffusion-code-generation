METERS_TO_FEET = 3.28084

def meters_to_feet(meters: float) -> float:
    return meters * METERS_TO_FEET

if __name__ == '__main__':
    sample_meters = 10
    result = meters_to_feet(sample_meters)
    print(result)