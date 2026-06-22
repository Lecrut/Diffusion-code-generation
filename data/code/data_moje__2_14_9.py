LITER_TO_ML = 1000.0
GALLON_TO_ML = 3785.411784
CUBIC_INCH_TO_ML = 16.387064

def convert_volumes_to_ml(measurements):
    if not isinstance(measurements, list):
        raise TypeError("Input must be a list")
    result = []
    for item in measurements:
        if not isinstance(item, (tuple, list)) or len(item) != 2:
            raise ValueError("Each measurement must be a tuple of (value, unit)")
        value, unit = item
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be a number")
        if value < 0:
            raise ValueError("Volume value cannot be negative")
        unit_str = str(unit).strip().lower()
        if unit_str in ('liter', 'liters', 'l'):
            converted = value * LITER_TO_ML
        elif unit_str in ('gallon', 'gallons', 'gal'):
            converted = value * GALLON_TO_ML
        elif unit_str in ('cubic inch', 'cubic inches', 'in3', 'ci'):
            converted = value * CUBIC_INCH_TO_ML
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        result.append(converted)
    return result

if __name__ == '__main__':
    sample_data = [
        (1, "liter"),
        (0.5, "gallons"),
        (10, "cubic inches"),
        (0, "liters"),
        (2.5, "gal")
    ]
    converted_results = convert_volumes_to_ml(sample_data)
    for original, converted in zip(sample_data, converted_results):
        print(f"{original} converted to {converted} ml")