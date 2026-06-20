UNIT_TO_METERS = {
    'm': 1.0,
    'meter': 1.0,
    'meters': 1.0,
    'km': 1000.0,
    'kilometer': 1000.0,
    'kilometers': 1000.0,
    'cm': 0.01,
    'centimeter': 0.01,
    'centimeters': 0.01,
    'mm': 0.001,
    'millimeter': 0.001,
    'millimeters': 0.001,
    'mi': 1609.344,
    'mile': 1609.344,
    'miles': 1609.344,
    'in': 0.0254,
    'inch': 0.0254,
    'inches': 0.0254,
    'ft': 0.3048,
    'foot': 0.3048,
    'feet': 0.3048,
    'yd': 0.9144,
    'yard': 0.9144,
    'yards': 0.9144,
}

def normalize_to_meters(value: float, unit: str) -> float:
    unit_lower = unit.lower()
    if unit_lower in UNIT_TO_METERS:
        return value * UNIT_TO_METERS[unit_lower]
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(normalize_to_meters(1.0, 'km'))
    print(normalize_to_meters(100.0, 'cm'))
    print(normalize_to_meters(1.0, 'mi'))
    print(normalize_to_meters(1.0, 'm'))
    print(normalize_to_meters(12.0, 'ft'))