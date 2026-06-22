def convert_volumes(volumes):
    return {k: v * 1000 for k, v in volumes.items()}

if __name__ == '__main__':
    sample_data = {'bathtub': 150, 'coffee_cup': 0.3, 'swimming_pool': 50000, 'shot_glass': 0.04}
    result = convert_volumes(sample_data)
    print(result)