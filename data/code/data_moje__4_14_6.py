def convert_distance(value: float, unit: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string")
    
    unit_lower = unit.strip().lower()
    
    if unit_lower == "meters" or unit_lower == "meter" or unit_lower == "m":
        factor = 1.0
    elif unit_lower == "kilometers" or unit_lower == "kilometer" or unit_lower == "km":
        factor = 1000.0
    elif unit_lower == "miles" or unit_lower == "mile" or unit_lower == "mi":
        factor = 1609.344
    elif unit_lower == "feet" or unit_lower == "foot" or unit_lower == "ft":
        factor = 0.3048
    else:
        raise ValueError(f"Unsupported unit: {unit}")
        
    meters = value * factor
    return round(meters, 6)

if __name__ == '__main__':
    result1 = convert_distance(1, "km")
    print(result1)
    
    result2 = convert_distance(1, "mile")
    print(result2)
    
    result3 = convert_distance(1, "ft")
    print(result3)
    
    result4 = convert_distance(1000, "m")
    print(result4)