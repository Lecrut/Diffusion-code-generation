def liters_to_milliliters(volume_dict):
    return {key: value * 1000 for key, value in volume_dict.items()}

if __name__ == '__main__':
    predefined_volumes = {
        'water': 1.5,
        'milk': 2.0,
        'juice': 0.75,
        'oil': 3.2
    }
    converted_volumes = liters_to_milliliters(predefined_volumes)
    print(converted_volumes)