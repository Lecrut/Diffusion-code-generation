def convert_distance(distance: float, target_unit: str) -> float:
    if not isinstance(target_unit, str):
        raise TypeError("Target unit must be a string.")
    
    target_unit_lower = target_unit.lower()
    
    if target_unit_lower in ("meter", "m", "meter", "metre"):
        return distance
    
    if distance == 0.0:
        return 0.0
    
    conversions = {
        "kilometer": 1000.0,
        "km": 1000.0,
        "mile": 1609.344,
        "mi": 1609.344,
        "foot": 0.3048,
        "ft": 0.3048,
        "inch": 0.0254,
        "in": 0.0254,
        "centimeter": 0.01,
        "cm": 0.01,
        "millimeter": 0.001,
        "mm": 0.001,
        "yard": 0.9144,
        "yd": 0.9144,
    }
    
    if target_unit_lower not in conversions:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    factor = conversions[target_unit_lower]
    result = distance / factor
    return result

if __name__ == '__main__':
    dist = 1000.0
    unit = "kilometer"
    res = convert_distance(dist, unit)
    print(res)