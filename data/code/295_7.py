class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        try:
            value_in_base = value * self.conversion_factors[from_unit]
            result = value_in_base / self.conversion_factors[to_unit]
            return result
        except KeyError:
            raise ValueError(f"Conversion path between {from_unit} and {to_unit} is undefined.")
if __name__ == '__main__':
    CONVERSION_DATA = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'gram': 0.001,
        'kilogram': 1000.0,
        'pound': 2.20462,
    }
    converter = UnitConverter(CONVERSION_DATA)
    value1 = 5000
    from1 = 'meter'
    to1 = 'kilometer'
    try:
        result1 = converter.convert(value1, from1, to1)
        print(f"{value1} {from1} is equal to {result1} {to1}")
    except ValueError as e:
        print(f"Error in Test 1: {e}")
    value2 = 2.5
    from2 = 'kilogram'
    to2 = 'pound'
    try:
        result2 = converter.convert(value2, from2, to2)
        print(f"{value2} {from2} is equal to {result2} {to2}")
    except ValueError as e:
        print(f"Error in Test 2: {e}")
    value3 = 10
    from3 = 'mile'
    to3 = 'mile'
    try:
        result3 = converter.convert(value3, from3, to3)
        print(f"{value3} {from3} is equal to {result3} {to3}")
    except ValueError as e:
        print(f"Error in Test 3: {e}")
    value4 = 100
    from4 = 'meter'
    to4 = 'furlong'
    try:
        result4 = converter.convert(value4, from4, to4)
        print(f"{value4} {from4} is equal to {result4} {to4}")
    except ValueError as e:
        print(f"Error in Test 4: {e}")