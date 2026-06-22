def cubic_meters_to_liters(cubic_meters):
    liters = cubic_meters * 1000
    return liters

if __name__ == '__main__':
    sample_volume_cubic_meters = 2.5
    converted_volume_liters = cubic_meters_to_liters(sample_volume_cubic_meters)
    print(converted_volume_liters)