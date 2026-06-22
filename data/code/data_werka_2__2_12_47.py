def cubic_meters_to_cubic_feet(meters):
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be a number")
    if meters < 0:
        raise ValueError("Volume cannot be negative")
    FEET_PER_METER = 3.28084
    return meters * (FEET_PER_METER ** 3)

if __name__ == '__main__':
    sample_values = [2.5, 12.0, 0.75, -3]
    for value in sample_values:
        try:
            result = cubic_meters_to_cubic_feet(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except (ValueError, TypeError) as e:
            print(e)