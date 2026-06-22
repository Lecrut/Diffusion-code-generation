def liters_to_milliliters(volumes):
    return {key: value * 1000 for key, value in volumes.items()}

if __name__ == '__main__':
    sample_volumes = {
        'water': 2.5,
        'milk': 1.0,
        'juice': 0.5
    }
    print(liters_to_milliliters(sample_volumes))