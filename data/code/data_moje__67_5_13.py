def liters_to_milliliters(volume_dict):
    return {key: value * 1000 for key, value in volume_dict.items()}

if __name__ == '__main__':
    sample_volumes = {
        'bucket': 5.0,
        'bottle': 0.5,
        'bathtub': 150.0,
        'cup': 0.25
    }
    converted_volumes = liters_to_milliliters(sample_volumes)
    print(converted_volumes)