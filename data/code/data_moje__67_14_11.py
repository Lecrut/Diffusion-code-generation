def liters_to_milliliters(volumes_liters):
    return [volume * 1000 for volume in volumes_liters]

if __name__ == '__main__':
    sample_volumes = [0.5, 1.0, 2.5, 3.75, 10.0]
    result = liters_to_milliliters(sample_volumes)
    print(result)