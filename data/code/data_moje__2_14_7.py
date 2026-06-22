LITERS_TO_ML = 1000
GALLONS_TO_ML = 3785.411784
CUBIC_INCHES_TO_ML = 16.387064

def convert_volumes_to_ml(measurements):
    if not isinstance(measurements, list):
        raise TypeError("Input must be a list of tuples (value, unit).")
    
    results = []
    for item in measurements:
        if not isinstance(item, (tuple, list)) or len(item) != 2:
            raise ValueError("Each measurement must be a tuple (value, unit).")
        
        value, unit = item
        
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be a number.")
        
        if value < 0:
            raise ValueError("Volume value cannot be negative.")
        
        unit_lower = str(unit).lower()
        
        if unit_lower in ("l", "liter", "liters"):
            ml_value = value * LITERS_TO_ML
        elif unit_lower in ("gal", "gallon", "gallons"):
            ml_value = value * GALLONS_TO_ML
        elif unit_lower in ("in3", "cubic inch", "cubic inches", "ci"):
            ml_value = value * CUBIC_INCHES_TO_ML
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        
        results.append(ml_value)
    
    return results

if __name__ == '__main__':
    sample_data = [
        (1.0, "liters"),
        (2.5, "gallons"),
        (100, "cubic inches"),
        (0, "liters"),
        (0.5, "gal"),
        (50, "in3")
    ]
    
    converted_results = convert_volumes_to_ml(sample_data)
    
    for original, converted in zip(sample_data, converted_results):
        print(f"{original[0]} {original[1]} -> {converted} ml")