def convert_liters_to_milliliters(volume_data):
    return {k: v * 1000 for k, v in volume_data.items()}

if __name__ == '__main__':
    volumes = {'cup': 1, 'bottle': 2, 'barrel': 159}
    result = convert_liters_to_milliliters(volumes)
    print(result)