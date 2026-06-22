def convert_distance(value, unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string")
    
    unit_lower = unit.lower().strip()
    
    if unit_lower not in ("meters", "kilometers", "miles", "feet"):
        raise ValueError("Unit must be one of: meters, kilometers, miles, feet")
    
    conversion_factors_to_meters = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "miles": 1609.344,
        "feet": 0.3048
    }
    
    if unit_lower not in conversion_factors_to_meters:
        raise ValueError("Unit must be one of: meters, kilometers, miles, feet")
        
    meters = value * conversion_factors_to_meters[unit_lower]
    
    return round(meters, 6)

if __name__ == '__main__':
    result = convert_distance(1, "miles")
    print(result)
    
    result2 = convert_distance(1000, "meters")
    print(result2)
    
    result3 = convert_distance(5280, "feet")
    print(result3)