def convert_to_milliliters(volumes):
    ml_per_unit = {
        'liters': 1000.0,
        'gallons': 3785.411784,
        'cubic_inches': 16.387064
    }
    result = []
    for volume, unit in volumes:
        if unit not in ml_per_unit:
            raise ValueError(f"Unsupported unit: {unit}")
        if volume == 0:
            result.append(0.0)
        elif volume < 0:
            result.append(-abs(volume) * ml_per_unit[unit])
        else:
            result.append(volume * ml_per_unit[unit])
    return result

if __name__ == '__main__':
    samples = [
        (1.0, 'liters'),
        (0.5, 'gallons'),
        (100, 'cubic_inches'),
        (0, 'liters'),
        (-1.0, 'gallons')
    ]
    converted = convert_to_milliliters(samples)
    for i, val in enumerate(converted):
        print(f"{val}")