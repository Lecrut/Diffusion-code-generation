import math

_UNIT_MAP = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344,
}

_TO_INCHES = {
    'm': 39.3701,
    'km': 39370.1,
    'cm': 3.93701,
    'mm': 0.393701,
    'in': 1.0,
    'ft': 12.0,
    'yd': 36.0,
    'mi': 63360.0,
}

_TO_METERS = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344,
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Units must be strings")
    
    u_from = from_unit.lower().strip()
    u_to = to_unit.lower().strip()
    
    if u_from not in _TO_METERS:
        raise ValueError(f"Unknown unit: {from_unit}")
    if u_to not in _TO_METERS:
        raise ValueError(f"Unknown unit: {to_unit}")
        
    meters = value * _TO_METERS[u_from]
    result = meters / _TO_METERS[u_to]
    
    if math.isinf(result) or math.isnan(result):
        raise OverflowError("Result is infinite or NaN")
        
    return result

if __name__ == '__main__':
    print(convert_length(1, 'km', 'm'))
    print(convert_length(12, 'in', 'ft'))
    print(convert_length(1, 'mi', 'km'))
    print(convert_length(100, 'cm', 'in'))
    print(convert_length(1, 'ft', 'cm'))