def convert_distance(value, from_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if not isinstance(from_unit, str):
        raise TypeError("Unit must be a string")
    
    supported_units = {"meters", "kilometers", "miles", "feet"}
    normalized_unit = from_unit.lower().strip()
    
    if normalized_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {from_unit}. Supported units are: {', '.join(sorted(supported_units))}")
    
    conversion_to_meters = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.344,
        "feet": 0.3048
    }
    
    meters_value = value * conversion_to_meters[normalized_unit]
    
    results = {}
    for unit, factor in conversion_to_meters.items():
        converted = meters_value / factor
        results[unit] = round(converted, 6)
    
    return results

if __name__ == "__main__":
    sample_value = 5.0
    sample_unit = "miles"
    result = convert_distance(sample_value, sample_unit)
    print(result)