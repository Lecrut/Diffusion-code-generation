import math

UNIT_DEFS = {
    'meter': {'factor': 1.0, 'offset': 0.0},
    'kilometer': {'factor': 1000.0, 'offset': 0.0},
    'centimeter': {'factor': 0.01, 'offset': 0.0},
    'millimeter': {'factor': 0.001, 'offset': 0.0},
    'inch': {'factor': 0.0254, 'offset': 0.0},
    'foot': {'factor': 0.3048, 'offset': 0.0},
    'mile': {'factor': 1609.344, 'offset': 0.0},
    'celsius': {'factor': 1.0, 'offset': 0.0},
    'fahrenheit': {'factor': 5.0/9.0, 'offset': 32.0},
}

class Converter:
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.from_def = UNIT_DEFS[from_unit]
        self.to_def = UNIT_DEFS[to_unit]

    def convert(self, value):
        base_value = (value - self.from_def['offset']) * self.from_def['factor']
        result = (base_value / self.to_def['factor']) + self.to_def['offset']
        return result

def convert_value(from_unit, to_unit, value):
    converter = Converter(from_unit, to_unit)
    return converter.convert(value)

if __name__ == '__main__':
    res1 = convert_value('kilometer', 'mile', 5.0)
    print(res1)
    
    res2 = convert_value('fahrenheit', 'celsius', 212.0)
    print(res2)
    
    res3 = convert_value('foot', 'meter', 10.0)
    print(res3)