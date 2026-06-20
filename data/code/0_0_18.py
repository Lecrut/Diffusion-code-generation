from typing import Union

def convert_length(value: Union[int, float], unit: str) -> float:
    conversion_factors = {
        'm': 1.0,
        'ft': 0.3048,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    value_in_meters = value * conversion_factors[unit]
    return value_in_meters

if __name__ == '__main__':
    print(convert_length(10, 'ft'))
    print(convert_length(5, 'm'))
    print(convert_length(1, 'mi'))