def convert_volume(volume, source_unit, target_unit="liter"):
    conversion_rates = {
        ("milliliter", "liter"): 0.001,
        ("liter", "milliliter"): 1000.0,
        ("milliliter", "gallon"): 0.000264172,
        ("gallon", "milliliter"): 3785.41,
        ("liter", "gallon"): 0.264172,
        ("gallon", "liter"): 3.78541,
        ("liter", "cubic_meter"): 0.001,
        ("cubic_meter", "liter"): 1000.0,
        ("milliliter", "cubic_meter"): 1e-6,
        ("cubic_meter", "milliliter"): 1e6,
        ("gallon", "cubic_meter"): 0.00378541,
        ("cubic_meter", "gallon"): 264.172,
        ("cup", "milliliter"): 236.588,
        ("milliliter", "cup"): 0.00422675,
        ("cup", "liter"): 0.236588,
        ("liter", "cup"): 4.22675,
        ("cup", "gallon"): 0.0625,
        ("gallon", "cup"): 16.0,
        ("cup", "cubic_meter"): 0.000236588,
        ("cubic_meter", "cup"): 4226.75,
        ("tablespoon", "milliliter"): 14.787,
        ("milliliter", "tablespoon"): 0.067628,
        ("tablespoon", "liter"): 0.014787,
        ("liter", "tablespoon"): 67.628,
        ("tablespoon", "gallon"): 0.00390625,
        ("gallon", "tablespoon"): 256.0,
        ("tablespoon", "cup"): 0.0625,
        ("cup", "tablespoon"): 16.0,
        ("tablespoon", "cubic_meter"): 1.4787e-5,
        ("cubic_meter", "tablespoon"): 67628.0,
    }
    
    source_unit = source_unit.lower()
    target_unit = target_unit.lower()
    
    if volume < 0:
        raise ValueError("Volume cannot be negative")
    
    if source_unit not in ["milliliter", "liter", "gallon", "cubic_meter", "cup", "tablespoon"]:
        raise ValueError(f"Unsupported source unit: {source_unit}")
        
    if target_unit not in ["milliliter", "liter", "gallon", "cubic_meter", "cup", "tablespoon"]:
        raise ValueError(f"Unsupported target unit: {target_unit}")
        
    if source_unit == target_unit:
        return volume
        
    key = (source_unit, target_unit)
    if key not in conversion_rates:
        raise ValueError(f"Conversion from {source_unit} to {target_unit} not supported")
        
    return volume * conversion_rates[key]

if __name__ == '__main__':
    print(convert_volume(1, "gallon"))
    print(convert_volume(1, "gallon", "milliliter"))
    print(convert_volume(1000, "milliliter", "liter"))
    print(convert_volume(1, "liter", "cup"))
    print(convert_volume(8, "cup", "tablespoon"))