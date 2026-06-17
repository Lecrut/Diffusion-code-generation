class UnitConverter:
    def __init__(self):
        self.base_units = {
            'length': 'meter',
            'mass': 'kilogram'
        }
        self.conversions = {
            ('length', 'meter'): 1.0,
            ('mass', 'kilogram'): 1.0
        }
    def register_base(self, dimension, unit):
        if dimension not in self.base_units:
            self.base_units[dimension] = unit
            self.conversions[(dimension, unit)] = 1.0
    def convert(self, value, from_unit, to_unit, dimensions):
        if from_unit == to_unit:
            return value
        if not all(d in self.base_units for d in dimensions):
            raise ValueError("Unsupported dimension(s) provided.")
        to_base = {}
        for dim in dimensions:
            if dim == 'length':
                if from_unit != self.base_units['length']:
                    if from_unit == 'meter':
                        to_base[dim] = value
                    else:
                        raise NotImplementedError(f"Conversion from {from_unit} to base length not explicitly defined.")
                else:
                    to_base[dim] = value
            elif dim == 'mass':
                if from_unit != self.base_units['mass']:
                    if from_unit == 'kilogram':
                        to_base[dim] = value
                    else:
                        raise NotImplementedError(f"Conversion from {from_unit} to base mass not explicitly defined.")
                else:
                    to_base[dim] = value
        result = {}
        for dim in dimensions:
            if dim == 'length':
                if to_unit == self.base_units['length']:
                    result[dim] = to_base['length']
                else:
                    raise NotImplementedError(f"Inverse length conversion from {self.base_units['length']} to {to_unit} not implemented.")
            elif dim == 'mass':
                if to_unit == self.base_units['mass']:
                    result[dim] = to_base['mass']
                else:
                    raise NotImplementedError(f"Inverse mass conversion from {self.base_units['mass']} to {to_unit} not implemented.")
        return result
if __name__ == '__main__':
    converter = UnitConverter()
    converter.register_base('length', 'meter')
    converter.register_base('mass', 'kilogram')
    print("--- Length Conversion (Meter Base) ---")
    try:
        result1 = converter.convert(10.0, 'meter', 'meter', ['length'])
        print(f"10.0 meters to meter: {result1}")
        result2 = converter.convert(5.0, 'meter', 'meter', ['length'])
        print(f"5.0 meters to meter: {result2}")
    except NotImplementedError as e:
        print(f"Length conversion error (expected if inverse not implemented): {e}")
    print("\n--- Mass Conversion (Kilogram Base) ---")
    try:
        result3 = converter.convert(10.0, 'kilogram', 'kilogram', ['mass'])
        print(f"10.0 kilograms to kilogram: {result3}")
    except NotImplementedError as e:
        print(f"Mass conversion error (expected if inverse not implemented): {e}")
    print("\n--- Attempting Conversion between different units (Fails due to strict base unit definition) ---")
    try:
        converter.convert(10, 'meter', 'kilogram', ['length', 'mass'])
    except NotImplementedError as e:
        print(f"Conversion failed as expected due to missing inverse implementation: {e}")