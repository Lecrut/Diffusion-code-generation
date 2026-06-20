def convert_length(value, from_unit, to_unit):
    base_units = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.344,
        "yd": 0.9144,
        "ft": 0.3048,
        "in": 0.0254
    }
    
    if from_unit not in base_units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in base_units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
        
    base_value = value * base_units[from_unit]
    result = base_value / base_units[to_unit]
    
    return result

if __name__ == '__main__':
    result = convert_length(1, "km", "mi")
    print(result)