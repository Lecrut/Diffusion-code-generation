def meters_to_feet(meters):
    conversion_factor = 3.28084
    return [round(meter * conversion_factor, 2) for meter in meters]

if __name__ == '__main__':
    sample_meters = [10.0, 25.0, 50.0]
    result_feet = meters_to_feet(sample_meters)
    print(result_feet)