def meters_to_feet(meters: float) -> float:
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_meters = 10
    feet_value = meters_to_feet(sample_meters)
    print(feet_value)