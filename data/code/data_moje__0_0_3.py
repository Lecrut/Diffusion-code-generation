from typing import Union

def convert_length(value: Union[int, float], unit: str) -> float:
    conversion_factors = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.34,
        'cm': 0.01,
        'mm': 0.001,
        'yd': 0.9144
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    if unit == 'm':
        return float(value)
    
    meters = value * conversion_factors[unit]
    return meters

if __name__ == '__main__':
    sample_value = 10
    sample_unit = 'ft'
    result = convert_length(sample_value, sample_unit)
    print(result)