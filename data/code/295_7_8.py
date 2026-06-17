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
        value_in_base = value * factor_from
        result = value_in_base / factor_to
        return result
if __name__ == '__main__':
    conversion_data = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "mile": 1609.34,
        "foot": 0.3048,
        "inch": 0.0254
    }
    converter = UnitConverter(conversion_data)
    value1 = 5.0
    from1 = "meter"
    to1 = "kilometer"
    result1 = converter.convert(value1, from1, to1)
    print(f"{value1} {from1} is equal to {result1} {to1}")
    value2 = 1.0
    from2 = "mile"
    to2 = "foot"
    result2 = converter.convert(value2, from2, to2)
    print(f"{value2} {from2} is equal to {result2} {to2}")
    value3 = 10.0
    from3 = "inch"
    to3 = "meter"
    result3 = converter.convert(value3, from3, to3)
    print(f"{value3} {from3} is equal to {result3} {to3}")
    value4 = 100
    from4 = "kilometer"
    to4 = "kilometer"
    result4 = converter.convert(value4, from4, to4)
    print(f"{value4} {from4} is equal to {result4} {to4}")