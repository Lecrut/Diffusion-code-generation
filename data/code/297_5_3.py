class UnitConverter:
    def __init__(self):
        self.length_factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34,
            'ft': 0.3048,
            'in': 0.0254
        }
        self.mass_factors = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 0.000001,
            'lb': 0.453592,
            'oz': 0.0283495
        }
    def convert(self, value, from_unit, to_unit, type):
        if type == 'length':
            if from_unit not in self.length_factors or to_unit not in self.length_factors:
                raise ValueError("Invalid length unit provided.")
            base_value = value * self.length_factors[from_unit]
            result = base_value / self.length_factors[to_unit]
            return result
        elif type == 'mass':
            if from_unit not in self.mass_factors or to_unit not in self.mass_factors:
                raise ValueError("Invalid mass unit provided.")
            base_value = value * self.mass_factors[from_unit]
            result = base_value / self.mass_factors[to_unit]
            return result
        else:
            raise ValueError("Invalid type specified. Must be 'length' or 'mass'.")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversions ---")
    val_l1 = 5.0
    from_l1 = 'km'
    to_l1 = 'm'
    result_l1 = converter.convert(val_l1, from_l1, to_l1, 'length')
    print(f"{val_l1} {from_l1} is equal to {result_l1} {to_l1}")
    val_l2 = 10.0
    from_l2 = 'mi'
    to_l2 = 'ft'
    result_l2 = converter.convert(val_l2, from_l2, to_l2, 'length')
    print(f"{val_l2} {from_l2} is equal to {result_l2} {to_l2}")
    val_l3 = 15.0
    from_l3 = 'cm'
    to_l3 = 'mm'
    result_l3 = converter.convert(val_l3, from_l3, to_l3, 'length')
    print(f"{val_l3} {from_l3} is equal to {result_l3} {to_l3}")
    print("\n--- Mass Conversions ---")
    val_m1 = 2.5
    from_m1 = 'kg'
    to_m1 = 'g'
    result_m1 = converter.convert(val_m1, from_m1, to_m1, 'mass')
    print(f"{val_m1} {from_m1} is equal to {result_m1} {to_m1}")
    val_m2 = 10.0
    from_m2 = 'lb'
    to_m2 = 'oz'
    result_m2 = converter.convert(val_m2, from_m2, to_m2, 'mass')
    print(f"{val_m2} {from_m2} is equal to {result_m2} {to_m2}")
    val_m3 = 500.0
    from_m3 = 'mg'
    to_m3 = 'kg'
    result_m3 = converter.convert(val_m3, from_m3, to_m3, 'mass')
    print(f"{val_m3} {from_m3} is equal to {result_m3} {to_m3}")