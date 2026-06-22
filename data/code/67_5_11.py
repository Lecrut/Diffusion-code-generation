def convert_liters_to_milliliters(volumes):
    return {k: v * 1000 for k, v in volumes.items()}

if __name__ == '__main__':
    sample_volumes = {
        "tank_a": 2.5,
        "tank_b": 0.75,
        "tank_c": 10.0,
        "tank_d": 0.05
    }
    converted = convert_liters_to_milliliters(sample_volumes)
    for key, value in converted.items():
        print(f"{key}: {value}")