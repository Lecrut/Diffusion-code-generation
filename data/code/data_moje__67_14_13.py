def convert_liters_to_milliliters(volumes_in_liters):
    return [volume * 1000 for volume in volumes_in_liters]

if __name__ == '__main__':
    sample_volumes = [1.5, 2, 0.5, 10]
    result = convert_liters_to_milliliters(sample_volumes)
    print(result)