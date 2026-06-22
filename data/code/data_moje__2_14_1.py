def convert_volumes_to_ml(volumes):
    LITERS_TO_ML = 1000.0
    GALLONS_TO_ML = 3785.411784
    CUBIC_INCHES_TO_ML = 16.387064
    results = []
    for value, unit in volumes:
        if value < 0:
            raise ValueError("Volume cannot be negative")
        if unit == 'liters':
            ml_value = value * LITERS_TO_ML
        elif unit == 'gallons':
            ml_value = value * GALLONS_TO_ML
        elif unit == 'cubic inches':
            ml_value = value * CUBIC_INCHES_TO_ML
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        results.append(ml_value)
    return results

if __name__ == '__main__':
    sample_data = [
        (1, 'liters'),
        (2.5, 'gallons'),
        (0, 'liters'),
        (100, 'cubic inches'),
        (0.5, 'liters')
    ]
    converted_values = convert_volumes_to_ml(sample_data)
    for original, result in zip(sample_data, converted_values):
        print(f"{original[0]} {original[1]} -> {result} ml")