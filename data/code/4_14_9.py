def convert_distance(value, source_unit, target_unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type")
    if not isinstance(source_unit, str) or not isinstance(target_unit, str):
        raise ValueError("Units must be strings")
    
    units = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.344,
        "feet": 0.3048
    }
    
    source_lower = source_unit.lower()
    target_lower = target_unit.lower()
    
    if source_lower not in units:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_lower not in units:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    meters = value * units[source_lower]
    result = meters / units[target_lower]
    return round(result, 6)

if __name__ == '__main__':
    sample_value = 1000
    source = "meters"
    target = "miles"
    print(convert_distance(sample_value, source, target))
    print(convert_distance(1, "miles", "kilometers"))
    print(convert_distance(5280, "feet", "meters"))
    print(convert_distance(1, "kilometers", "feet"))