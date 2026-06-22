def convert_length_measurements(lengths, unit):
    meters_per_unit = {
        'kilometers': 1000.0,
        'miles': 1609.34,
        'yards': 0.9144,
        'inches': 0.0254,
        'feet': 0.3048,
        'meters': 1.0,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    feet_per_meter = 3.28084
    results = []
    for length in lengths:
        if unit not in meters_per_unit:
            raise ValueError(f"Unsupported unit: {unit}")
        meters = length * meters_per_unit[unit]
        feet = meters * feet_per_meter
        results.append((meters, feet))
    return results

if __name__ == '__main__':
    sample_lengths = [1.0, 5.5, 10.2, 100.0]
    sample_unit = 'kilometers'
    converted = convert_length_measurements(sample_lengths, sample_unit)
    for meters, feet in converted:
        print(f"{meters} meters, {feet} feet")