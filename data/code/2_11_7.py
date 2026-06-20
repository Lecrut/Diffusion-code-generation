CONVERSION_FACTORS = {
    "cubic_meter": 1.0,
    "liter": 0.001,
    "milliliter": 0.000001,
    "gallon_us": 0.00378541,
    "cubic_foot": 0.0283168,
    "cubic_inch": 0.0000163871,
    "barrel_oil": 0.158987,
}

def standardize_volume(measurements, base_unit="cubic_meter"):
    if base_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported base unit: {base_unit}")
    
    base_factor = CONVERSION_FACTORS[base_unit]
    standardized = {}
    
    for item, (value, unit) in measurements.items():
        if unit not in CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit for item {item}: {unit}")
        
        item_factor = CONVERSION_FACTORS[unit]
        value_in_base = (value * item_factor) / base_factor
        standardized[item] = value_in_base
    
    return standardized

if __name__ == "__main__":
    sample_data = {
        "water": (10.0, "liter"),
        "sand": (5500.0, "milliliter"),
        "oil": (2.5, "gallon_us"),
        "gravel": (100.0, "cubic_foot")
    }
    
    result = standardize_volume(sample_data, "cubic_meter")
    print(result)