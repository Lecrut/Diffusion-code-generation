def liters_to_milliliters(volumes_dict):
    return {key: value * 1000 for key, value in volumes_dict.items()}

if __name__ == '__main__':
    sample_volumes = {
        'jug_a': 1.5,
        'jug_b': 0.75,
        'jug_c': 2.0,
        'jug_d': 0.25
    }
    converted_volumes = liters_to_milliliters(sample_volumes)
    print(converted_volumes)