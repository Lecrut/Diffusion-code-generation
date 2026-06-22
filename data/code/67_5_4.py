def convert_liters_to_milliliters(volume_measurements):
    return {name: volume * 1000 for name, volume in volume_measurements.items()}

if __name__ == '__main__':
    sample_data = {
        "bottle": 2.5,
        "bucket": 10.0,
        "gallon_jug": 3.785,
        "tank": 150.25
    }
    converted_values = convert_liters_to_milliliters(sample_data)
    print(converted_values)