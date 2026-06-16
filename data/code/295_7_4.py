class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]
        base_value = value / factor_from
        result = base_value * factor_to
        return result
if __name__ == '__main__':
    conversion_data = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'gram': 0.001,
        'kilogram': 1000.0,
        'liter': 3.78541,
        'milliliter': 1000.0
    }
    converter = UnitConverter(conversion_data)
    value1 = 500.0
    from_unit1 = 'meter'
    to_unit1 = 'kilometer'
    result1 = converter.convert(value1, from_unit1, to_unit1)
    print(f"{value1} {from_unit1} is equal to {result1} {to_unit1}")
    value2 = 2.5
    from_unit2 = 'kilogram'
    to_unit2 = 'gram'
    result2 = converter.convert(value2, from_unit2, to_unit2)
    print(f"{value2} {from_unit2} is equal to {result2} {to_unit2}")
    value3 = 10.0
    from_unit3 = 'liter'
    to_unit3 = 'milliliter'
    result3 = converter.convert(value3, from_unit3, to_unit3)
    print(f"{value3} {from_unit3} is equal to {result3} {to_unit3}")
    value4 = 100.0
    from_unit4 = 'meter'
    to_unit4 = 'meter'
    result4 = converter.convert(value4, from_unit4, to_unit4)
    print(f"{value4} {from_unit4} is equal to {result4} {to_unit4}")
    try:
        converter.convert(10, 'meter', 'furlong')
    except ValueError as e:
        print(f"Error caught: {e}")