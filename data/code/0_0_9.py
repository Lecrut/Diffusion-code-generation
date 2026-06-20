from typing import Union, Optional

CONVERSION_RATES = {
    'm': 1.0,
    'ft': 0.3048,
    'in': 0.0254,
    'cm': 0.01,
    'km': 1000.0,
    'mi': 1609.344,
    'yd': 0.9144,
}

def convert_length(value: Union[int, float], from_unit: str, to_unit: str = 'm') -> float:
    if from_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    value_in_meters = value * CONVERSION_RATES[from_unit]
    return value_in_meters / CONVERSION_RATES[to_unit]

if __name__ == '__main__':
    print(convert_length(10, 'ft', 'm'))
    print(convert_length(5, 'm', 'ft'))
    print(convert_length(1, 'km', 'mi'))