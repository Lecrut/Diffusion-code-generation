def convert_liters_to_milliliters(volumes):
    return [volume * 1000 for volume in volumes]

if __name__ == '__main__':
    sample_volumes = [1.5, 2.0, 0.25, 10]
    result = convert_liters_to_milliliters(sample_volumes)
    print(result)