def validate_volume(meters):
    if not isinstance(meters, (int, float)):
        raise TypeError("Volume must be a number")
    if meters < 0:
        raise ValueError("Volume cannot be negative")

def cubic_meters_to_cubic_feet(meters):
    validate_volume(meters)
    FEET_PER_METER = 3.28084
    return meters * (FEET_PER_METER ** 3)

if __name__ == '__main__':
    sample_values = [1.5, 7.2, 20.0, 0]
    for value in sample_values:
        try:
            result = cubic_meters_to_cubic_feet(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except (ValueError, TypeError) as e:
            print(e)