def cubic_meters_to_cubic_feet(meters):
    if meters < 0:
        raise ValueError("Volume cannot be negative")
    conversion_factors = {
        'meters_to_feet': 3.28084
    }
    feet_per_meter = conversion_factors['meters_to_feet']
    return meters * (feet_per_meter ** 3)

if __name__ == '__main__':
    sample_values = [1, 5, 10, 0]
    for value in sample_values:
        try:
            result = cubic_meters_to_cubic_feet(value)
            print(f"{value} cubic meters is {result:.2f} cubic feet")
        except ValueError as e:
            print(e)