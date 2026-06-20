def convert_distance(value: float, source_unit: str, target_unit: str) -> float:
    valid_units = {"meters", "kilometers", "miles", "feet"}
    if source_unit not in valid_units:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_unit not in valid_units:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    meters_per_unit = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.344,
        "feet": 0.3048
    }
    
    meters_value = value * meters_per_unit[source_unit]
    result = meters_value / meters_per_unit[target_unit]
    return round(result, 6)

if __name__ == '__main__':
    print(convert_distance(1000, "meters", "feet"))
    print(convert_distance(1.5, "miles", "kilometers"))
    print(convert_distance(5000, "feet", "meters"))
    print(convert_distance(1, "kilometers", "miles"))