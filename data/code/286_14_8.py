def yards_to_meters(yards):
    if not isinstance(yards, (int, float)) or yards < 0:
        raise ValueError("Invalid input: Input must be a non-negative number")
    return yards * 0.9144

if __name__ == '__main__':
    yard_measurements = [1.0, 5.0, 10.5, 20.0]
    meter_measurements = [yards_to_meters(y) for y in yard_measurements]
    print(meter_measurements)