def validate_yards(yards):
    if not all(isinstance(y, (int, float)) and y >= 0 for y in yards):
        raise ValueError("All values must be non-negative numbers")

def yards_to_meters(yards):
    validate_yards(yards)
    return [y * 0.9144 for y in yards]

if __name__ == '__main__':
    measurements = [1.0, 5.0, 10.5, 100.0]
    meters_measurements = yards_to_meters(measurements)
    print(meters_measurements)