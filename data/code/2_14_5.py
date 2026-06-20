LITER_TO_ML = 1000.0
GALLON_TO_ML = 3785.411784
CUBIC_INCH_TO_ML = 16.387064

def convert_volumes_to_ml(measurements):
    if not measurements:
        return []
    result = []
    for value, unit in measurements:
        if value < 0:
            raise ValueError("Volume cannot be negative")
        if value == 0:
            result.append(0.0)
            continue
        unit_lower = unit.lower()
        if unit_lower == "liters" or unit_lower == "liter":
            converted = value * LITER_TO_ML
        elif unit_lower == "gallons" or unit_lower == "gallon":
            converted = value * GALLON_TO_ML
        elif unit_lower == "cubic inches" or unit_lower == "cubic inch":
            converted = value * CUBIC_INCH_TO_ML
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        result.append(converted)
    return result

if __name__ == '__main__':
    sample_data = [
        (1.0, "liters"),
        (0.0, "gallons"),
        (2.5, "cubic inches"),
        (0.5, "gallon"),
        (100, "liter")
    ]
    try:
        ml_values = convert_volumes_to_ml(sample_data)
        for original, unit in sample_data:
            print(f"{original} {unit} = {ml_values[sample_data.index((original, unit))]:.4f} mL")
    except ValueError as e:
        print(f"Error: {e}")