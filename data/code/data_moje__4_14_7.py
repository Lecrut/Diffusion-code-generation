def convert_distance(value, source_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a numeric type")
    if not isinstance(source_unit, str):
        raise TypeError("Source unit must be a string")
    
    source_unit_lower = source_unit.lower().strip()
    
    if source_unit_lower == "meter":
        meters = float(value)
    elif source_unit_lower == "kilometer":
        meters = float(value) * 1000.0
    elif source_unit_lower == "mile":
        meters = float(value) * 1609.344
    elif source_unit_lower == "foot":
        meters = float(value) / 3.28084
    else:
        raise ValueError(f"Invalid source unit: {source_unit}")
    
    units = ["meter", "kilometer", "mile", "foot"]
    
    results = {}
    for unit in units:
        if unit == "meter":
            results[unit] = meters
        elif unit == "kilometer":
            results[unit] = meters / 1000.0
        elif unit == "mile":
            results[unit] = meters / 1609.344
        elif unit == "foot":
            results[unit] = meters * 3.28084
    
    formatted_results = {k: round(v, 6) for k, v in results.items()}
    
    if source_unit_lower == "meter":
        return formatted_results["meter"]
    elif source_unit_lower == "kilometer":
        return formatted_results["kilometer"]
    elif source_unit_lower == "mile":
        return formatted_results["mile"]
    elif source_unit_lower == "foot":
        return formatted_results["foot"]
    return 0.0

if __name__ == "__main__":
    val_miles = 5.0
    unit = "mile"
    result = convert_distance(val_miles, unit)
    print(result)