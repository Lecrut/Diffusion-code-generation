def meters_to_feet(meters):
    feet_per_meter = 3.28084
    return meters * feet_per_meter

if __name__ == '__main__':
    sample_meters = 10
    result_feet = meters_to_feet(sample_meters)
    print(result_feet)