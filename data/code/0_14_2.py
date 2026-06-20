_LENGTH_FACTORS = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344
}

def convert_length(value, source_unit, target_unit):
    source_key = source_unit.lower()
    target_key = target_unit.lower()
    if source_key not in _LENGTH_FACTORS:
        raise ValueError("Invalid source unit")
    if target_key not in _LENGTH_FACTORS:
        raise ValueError("Invalid target unit")
    value_in_meters = value * _LENGTH_FACTORS[source_key]
    return value_in_meters / _LENGTH_FACTORS[target_key]

class LengthUnitConverter:
    def __init__(self):
        self.factors = _LENGTH_FACTORS
    
    def convert(self, amount, from_u, to_u):
        fu = from_u.lower()
        tu = to_u.lower()
        if fu not in self.factors:
            raise LookupError("Bad from unit")
        if tu not in self.factors:
            raise LookupError("Bad to unit")
        return amount * self.factors[fu] / self.factors[tu]
    
    def convert_batch(self, items):
        results = []
        for val, src, dst in items:
            results.append(self.convert(val, src, dst))
        return results

if __name__ == '__main__':
    converter = LengthUnitConverter()
    print(converter.convert(1, 'mi', 'km'))
    print(converter.convert(1, 'm', 'ft'))
    print(convert_length(5, 'km', 'm'))
    print(convert_length(100, 'cm', 'in'))
    batch = [(1, 'ft', 'in'), (1, 'yd', 'ft'), (1, 'mi', 'km')]
    print(converter.convert_batch(batch))