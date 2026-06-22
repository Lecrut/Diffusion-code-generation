def liters_to_milliliters(volume_dict):
    return {key: value * 1000 for key, value in volume_dict.items()}

if __name__ == '__main__':
    sample_volumes = {"bucket": 2.5, "glass": 0.25, "pool": 50000.0}
    converted = liters_to_milliliters(sample_volumes)
    print(converted)