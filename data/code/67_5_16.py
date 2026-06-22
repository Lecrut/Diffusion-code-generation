def convert_liters_to_milliliters(volumes):
    return {key: value * 1000 for key, value in volumes.items()}

if __name__ == '__main__':
    sample_volumes = {
        'water': 1.5,
        'milk': 2.0,
        'juice': 0.5
    }
    print(convert_liters_to_milliliters(sample_volumes))