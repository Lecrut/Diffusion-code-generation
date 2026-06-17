class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'length': {
                'm': 1.0,
                'km': 1000.0,
                'cm': 0.01,
                'mm': 0.001,
                'in': 0.0254,
                'ft': 0.3048,
                'yd': 0.9144,
                'mi': 1609.34
            },
            'mass': {
                'kg': 1.0,
                'g': 0.001,
                'mg': 0.000001,
                'lb': 0.453592,
                'oz': 0.0283495
            },
            'volume': {
                'L': 1.0,
                'mL': 0.001,
                'm3': 1.0,
                'gal': 3.78541,
                'qt': 0.946353
            }
        }
    def _get_unit_type(self, unit):
        for type_data in self.conversion_factors.values():
            if unit in type_data:
                return type_data
        raise ValueError(f"Unknown unit: {unit}")
    def convert(self, value, from_unit, to_unit, unit_type):
        if unit_type not in self.conversion_factors:
            raise ValueError("Invalid unit type specified.")
        if from_unit not in self.conversion_factors[unit_type] or to_unit not in self.conversion_factors[unit_type]:
            raise ValueError(f"One or both units ({from_unit}, {to_unit}) are not supported for type {unit_type}.")
        if from_unit == to_unit:
            return value
        factor_from = self.conversion_factors[unit_type][from_unit]
        factor_to = self.conversion_factors[unit_type][to_unit]
        value_in_base = value * factor_from
        result = value_in_base / factor_to
        return result
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion (m to km) ---")
    try:
        length_result = converter.convert(1000, 'm', 'km', 'length')
        print(f"1000 m is {length_result} km")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (kg to lb) ---")
    try:
        mass_result = converter.convert(5, 'kg', 'lb', 'mass')
        print(f"5 kg is {mass_result} lb")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Volume Conversion (L to m3) ---")
    try:
        volume_result = converter.convert(2.5, 'L', 'm3', 'volume')
        print(f"2.5 L is {volume_result} m3")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Length Conversion (in to cm) ---")
    try:
        length_result = converter.convert(10, 'in', 'cm', 'length')
        print(f"10 in is {length_result} cm")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Error Handling Example ---")
    try:
        converter.convert(10, 'm', 'kg', 'length')
    except ValueError as e:
        print(f"Caught expected error: {e}")
    try:
        converter.convert(10, 'unknown_unit', 'm', 'length')
    except ValueError as e:
        print(f"Caught expected error: {e}")