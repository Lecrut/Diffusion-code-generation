def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    conversions = {
        'mL': {'mL': 1.0, 'L': 0.001, 'm3': 1e-6, 'gal': 0.000264172},
        'L': {'mL': 1000.0, 'L': 1.0, 'm3': 0.001, 'gal': 0.264172},
        'm3': {'mL': 1e6, 'L': 1000.0, 'm3': 1.0, 'gal': 264.172},
        'gal': {'mL': 3785.41, 'L': 3.78541, 'm3': 0.00378541, 'gal': 1.0}
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
    return value * conversions[from_unit][to_unit]

if __name__ == '__main__':
    sample_liters = 1.5
    converted_to_ml = convert_volume(sample_liters, 'L', 'mL')
    print(converted_to_ml)

    sample_m3 = 0.5
    converted_to_gal = convert_volume(sample_m3, 'm3', 'gal')
    print(converted_to_gal)

    sample_gal = 2.0
    converted_to_L = convert_volume(sample_gal, 'gal', 'L')
    print(converted_to_L)