def liters_to_milliliters(volumes):
    return [v * 1000 for v in volumes]

if __name__ == '__main__':
    sample_volumes = [1.5, 2.0, 0.75]
    result = liters_to_milliliters(sample_volumes)
    print(result)