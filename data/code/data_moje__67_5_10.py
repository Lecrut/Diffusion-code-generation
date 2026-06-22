def liters_to_milliliters(volume_dict):
    return {key: value * 1000 for key, value in volume_dict.items()}

if __name__ == '__main__':
    sample_volumes = {'tank_a': 5.0, 'tank_b': 12.5, 'tank_c': 0.25}
    print(liters_to_milliliters(sample_volumes))