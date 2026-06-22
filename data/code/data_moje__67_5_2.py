def convert_volumes_to_ml(volume_dict):
    return {k: v * 1000 for k, v in volume_dict.items()}

if __name__ == '__main__':
    volumes = {'water': 1.5, 'milk': 0.5, 'juice': 2.0}
    result = convert_volumes_to_ml(volumes)
    print(result)