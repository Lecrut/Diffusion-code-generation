UNIT_FACTORS = {
    'meter': 1.0,
    'm': 1.0,
    'kilometer': 1000.0,
    'km': 1000.0,
    'mile': 1609.344,
    'mi': 1609.344,
    'foot': 0.3048,
    'ft': 0.3048,
    'inch': 0.0254,
    'in': 0.0254,
    'centimeter': 0.01,
    'cm': 0.01,
    'millimeter': 0.001,
    'mm': 0.001,
    'yard': 0.9144,
    'yd': 0.9144,
}

def normalize_unit_name(unit):
    return unit.lower().strip()

def get_conversion_factor(unit):
    normalized = normalize_unit_name(unit)
    if normalized in UNIT_FACTORS:
        return UNIT_FACTORS[normalized]
    raise ValueError(f"Unsupported unit: {unit}")

def convert_distance(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value < 0:
        raise ValueError("Distance cannot be negative")
    from_factor = get_conversion_factor(from_unit)
    to_factor = get_conversion_factor(to_unit)
    value_in_meters = value * from_factor
    result = value_in_meters / to_factor
    return result

class DistanceConverter:
    def __init__(self):
        self.conversion_log = []
    
    def convert(self, value, from_unit, to_unit):
        result = convert_distance(value, from_unit, to_unit)
        self.conversion_log.append({
            'value': value,
            'from': from_unit,
            'to': to_unit,
            'result': result
        })
        return result
    
    def get_last_conversion(self):
        if self.conversion_log:
            return self.conversion_log[-1]
        return None

if __name__ == '__main__':
    converter = DistanceConverter()
    result1 = converter.convert(1, 'mile', 'km')
    print(result1)
    result2 = converter.convert(100, 'cm', 'm')
    print(result2)
    result3 = converter.convert(5, 'ft', 'm')
    print(result3)