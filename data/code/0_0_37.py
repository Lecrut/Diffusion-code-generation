from typing import Union

def convert_length(value: float, unit: str) -> float:
    meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144
    }
    
    if unit not in meters:
        raise ValueError(f"Unsupported unit: {unit}")
    
    value_in_meters = value * meters[unit]
    
    return value_in_meters

if __name__ == '__main__':
    result1 = convert_length(1, 'km')
    print(result1)
    
    result2 = convert_length(100, 'cm')
    print(result2)
    
    result3 = convert_length(1, 'ft')
    print(result3)