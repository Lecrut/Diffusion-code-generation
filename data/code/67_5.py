def liters_to_milliliters(volume_dict):
    return {k: v * 1000 for k, v in volume_dict.items()}

if __name__ == '__main__':
    sample_volumes = {
        'water': 1.5,
        'milk': 2.0,
        'juice': 0.75,
        'soda': 1.0
    }
    converted_volumes = liters_to_milliliters(sample_volumes)
    print(converted_volumes)