import math

def normalize_to_meters(value: float, unit: str) -> float:
    value = float(value)
    unit = unit.lower().strip()
    conversion_factors = {'m': 1.0, 'km': 1000.0, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.344, 'ft': 0.3048, 'in': 0.0254, 'yd': 0.9144}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return value * conversion_factors[unit]

def format_distance(meters: float, precision: int=2) -> str:
    meters = float(meters)
    if abs(meters) < 0.001:
        return f'{meters * 1000:.{precision}f} mm'
    elif abs(meters) < 1:
        return f'{meters * 100:.{precision}f} cm'
    elif abs(meters) < 1000:
        return f'{meters:.{precision}f} m'
    else:
        return f'{meters / 1000:.{precision}f} km'
if __name__ == '__main__':
    samples = [(5.0, 'km'), (150.0, 'cm'), (0.005, 'km'), (3.28, 'ft'), (1.0, 'in'), (10000.0, 'mm')]
    for val, unit in samples:
        meters = normalize_to_meters(val, unit)
        formatted = format_distance(meters)
        print(f'{val} {unit} = {meters} m -> {formatted}')