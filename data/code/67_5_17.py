def convert_volumes_to_milliliters(volume_dict):
    return {k: v * 1000 for k, v in volume_dict.items()}

if __name__ == '__main__':
    volumes = {'a': 1.5, 'b': 2.0, 'c': 0.75}
    result = convert_volumes_to_milliliters(volumes)
    print(result)