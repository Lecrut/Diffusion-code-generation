def convert_liter_to_milliliter(volume_data):
    return {unit: value * 1000 for unit, value in volume_data.items()}

if __name__ == '__main__':
    sample_volumes = {"tank_a": 5, "tank_b": 12.5, "tank_c": 0.25}
    print(convert_liter_to_milliliter(sample_volumes))