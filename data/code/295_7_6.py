class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        if from_unit == 'm' and to_unit == 'km':
            return value * 1000
        elif from_unit == 'km' and to_unit == 'm':
            return value / 1000
        elif from_unit == 'kg' and to_unit == 'g':
            return value * 1000
        elif from_unit == 'g' and to_unit == 'kg':
            return value / 1000
        else:
            raise NotImplementedError(f"Conversion from {from_unit} to {to_unit} is not implemented in this sample system.")
if __name__ == '__main__':
    conversion_data = {
        ('m', 'km'): 1000,
        ('km', 'm'): 0.001,
        ('kg', 'g'): 1000,
        ('g', 'kg'): 0.001
    }
    converter = UnitConverter(conversion_data)
    value1 = 5
    from_unit1 = 'm'
    to_unit1 = 'km'
    try:
        result1 = converter.convert(value1, from_unit1, to_unit1)
        print(f"{value1} {from_unit1} is equal to {result1} {to_unit1}")
    except (ValueError, NotImplementedError) as e:
        print(f"Error for Test 1: {e}")
    value2 = 2.5
    from_unit2 = 'kg'
    to_unit2 = 'g'
    try:
        result2 = converter.convert(value2, from_unit2, to_unit2)
        print(f"{value2} {from_unit2} is equal to {result2} {to_unit2}")
    except (ValueError, NotImplementedError) as e:
        print(f"Error for Test 2: {e}")
    value3 = 10
    from_unit3 = 'm'
    to_unit3 = 'm'
    try:
        result3 = converter.convert(value3, from_unit3, to_unit3)
        print(f"{value3} {from_unit3} is equal to {result3} {to_unit3}")
    except (ValueError, NotImplementedError) as e:
        print(f"Error for Test 3: {e}")
    value4 = 10
    from_unit4 = 'm'
    to_unit4 = 'kg'
    try:
        result4 = converter.convert(value4, from_unit4, to_unit4)
        print(f"{value4} {from_unit4} is equal to {result4} {to_unit4}")
    except (ValueError, NotImplementedError) as e:
        print(f"Error for Test 4: {e}")