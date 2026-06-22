def convert_liters_to_milliliters(volumes_liters):
    return [volume * 1000 for volume in volumes_liters]

if __name__ == '__main__':
    sample_volumes = [1.5, 2.0, 0.75, 3.25]
    converted_volumes = convert_liters_to_milliliters(sample_volumes)
    print(converted_volumes)