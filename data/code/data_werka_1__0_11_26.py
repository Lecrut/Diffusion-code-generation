def meters_to_feet(meters):
    feet_per_meter = 3.28084
    return meters * feet_per_meter

if __name__ == '__main__':
    sample_value_meters = 10
    converted_value_feet = meters_to_feet(sample_value_meters)
    print(converted_value_feet)