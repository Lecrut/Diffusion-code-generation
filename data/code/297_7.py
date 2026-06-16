import math
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
    def convert(self, value, from_unit, to_unit, dimension):
        if from_unit == to_unit:
            return value
        if dimension not in self.base_units:
            raise ValueError(f"Dimension {dimension} is not supported.")
        if from_unit not in self.conversions or to_unit not in self.conversions:
            raise ValueError("Units not registered.")
        from_base = None
        to_base = None
        if dimension == 'length':
            from_base = self.base_units['length']
            to_base = self.base_units['length']
        elif dimension == 'mass':
            from_base = self.base_units['mass']
            to_base = self.base_units['mass']
        else:
            raise ValueError("Unsupported dimension for conversion.")
        if from_unit == from_base:
            value_in_base = value
        elif (dimension, from_unit) in self.conversions:
            value_in_base = value * self.conversions[(dimension, from_unit)]
        else:
            raise ValueError(f"Conversion factor for {from_unit} not found.")
        if to_unit == to_base:
            return value_in_base
        elif (dimension, to_unit) in self.conversions:
            result = value_in_base / self.conversions[(dimension, to_unit)]
            return result
        else:
            raise ValueError(f"Conversion factor for {to_unit} not found.")
if __name__ == '__main__':
    converter = UnitConverter()
    converter.register_base('length', 'meter')
    converter.register_base('mass', 'kilogram')
    converter.conversions[('length', 'foot')] = 3.28084
    converter.conversions[('foot', 'meter')] = 1 / 3.28084
    converter.conversions[('mass', 'pound')] = 2.20462
    converter.conversions[('pound', 'mass')] = 1 / 2.20462
    print("--- Length Conversion (Meter to Foot) ---")
    length_value = 10.0
    from_unit = 'meter'
    to_unit = 'foot'
    dimension = 'length'
    try:
        result = converter.convert(length_value, from_unit, to_unit, dimension)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (Kilogram to Pound) ---")
    mass_value = 5.0
    from_unit = 'kilogram'
    to_unit = 'pound'
    dimension = 'mass'
    try:
        result = converter.convert(mass_value, from_unit, to_unit, dimension)
        print(f"{mass_value} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Identity Conversion (Meter to Meter) ---")
    length_value = 5.0
    from_unit = 'meter'
    to_unit = 'meter'
    dimension = 'length'
    try:
        result = converter.convert(length_value, from_unit, to_unit, dimension)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")