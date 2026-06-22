def convert_liters_to_milliliters(volume_dict):
    converted_dict = {}
    for key, value in volume_dict.items():
        converted_dict[key] = value * 1000
    return converted_dict

if __name__ == '__main__':
    sample_volumes = {
        'bucket': 5.0,
        'bottle': 1.5,
        'cup': 0.25,
        'tank': 100.0,
        'dropper': 0.01
    }
    result = convert_liters_to_milliliters(sample_volumes)
    print(result)