def convert_cubic_meters_to_liters(cubic_meters):
    liters_per_cubic_meter = 1000
    return cubic_meters * liters_per_cubic_meter

if __name__ == '__main__':
    sample_volume_cubic_meters = 5.0
    converted_volume_liters = convert_cubic_meters_to_liters(sample_volume_cubic_meters)
    print(converted_volume_liters)