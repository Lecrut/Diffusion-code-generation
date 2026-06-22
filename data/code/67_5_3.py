def convert_liters_to_milliliters(volume_dict):
    return {key: value * 1000 for key, value in volume_dict.items()}

if __name__ == '__main__':
    sample_volumes = {'water': 2.5, 'milk': 1.5, 'juice': 3.0}
    converted = convert_liters_to_milliliters(sample_volumes)
    print(converted)