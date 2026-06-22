def cubic_meters_to_cubic_feet(meters):
    if meters < 0:
        raise ValueError("Volume cannot be negative")
    feet_per_meter = 3.28084
    return meters * (feet_per_meter ** 3)

if __name__ == '__main__':
    sample_values = [0.5, 12.3, 45.67, -1]
    for value in sample_values:
        try:
            result = cubic_meters_to_cubic_feet(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except ValueError as e:
            print(e)