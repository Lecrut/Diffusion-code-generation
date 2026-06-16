class UnitConverter:
    def __init__(self):
        self.base_units = {
            'length': 'meter',
            'mass': 'kilogram'
        }
        self.conversions = {
            ('length', 'length'): 1.0,
            ('mass', 'mass'): 1.0
        }
    def register_base(self, dimension, unit):
        if dimension not in self.base_units:
            self.base_units[dimension] = unit
        else:
            pass
    def convert(self, value, from_unit, to_unit, dimensions):
        if from_unit == to_unit:
            return value
        if not all(d in self.base_units for d in dimensions):
            raise ValueError("Unsupported dimension(s) provided.")
        base_value = {}
        for dim in dimensions:
            if dim == 'length':
                base_unit = self.base_units['length']
            elif dim == 'mass':
                base_unit = self.base_units['mass']
            else:
                raise ValueError(f"Unsupported dimension for conversion: {dim}")
            if from_unit == base_unit:
                base_value[dim] = value
            else:
                base_value[dim] = value                                      
        result = {}
        for dim in dimensions:
            if dim == 'length':
                if to_unit == self.base_units['length']:
                    result[dim] = base_value[dim]
                else:
                    result[dim] = base_value[dim] * 1.0                                                            
            elif dim == 'mass':
                if to_unit == self.base_units['mass']:
                    result[dim] = base_value[dim]
                else:
                    result[dim] = base_value[dim] * 1.0
        return result
if __name__ == '__main__':
    converter = UnitConverter()
    converter.register_base('length', 'meter')
    converter.register_base('mass', 'kilogram')
    print("--- Length Conversion (Meter Base) ---")
    try:
        result1 = converter.convert(5, 'meter', 'meter', ['length'])
        print(f"5 meters to meters: {result1}")
        result2 = converter.convert(1, 'mile', 'meter', ['length'])
        print(f"1 mile to meters (Structural Test): {result2}")
    except ValueError as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversion (Kilogram Base) ---")
    try:
        result3 = converter.convert(10, 'kilogram', 'kilogram', ['mass'])
        print(f"10 kilograms to kilograms: {result3}")
    except ValueError as e:
        print(f"Error during mass conversion: {e}")