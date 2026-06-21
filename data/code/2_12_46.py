def cubic_meters_to_cubic_feet(meters):
    if meters < 0:
        raise ValueError("Volume cannot be negative")
    feet_per_meter = 3.28084
    return meters * (feet_per_meter ** 3)

if __name__ == '__main__':
    sample_values = [1, 5, 10, 20]
    for value in sample_values:
        print(f"{value} cubic meters is {cubic_meters_to_cubic_feet(value):.4f} cubic feet")