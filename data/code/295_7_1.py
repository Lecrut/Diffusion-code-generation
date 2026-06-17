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
            raise ValueError("Conversion failed due to missing factor.")
if __name__ == '__main__':
    conversion_data = {
        "meter_to_cm": 100.0,
        "kg_to_g": 1000.0,
        "mile_to_km": 1.60934,
        "hour_to_minute": 60.0
    }
    converter = UnitConverter(conversion_data)
    value1 = 5.0
    from_unit1 = "meter"
    to_unit1 = "cm"
    class SimpleConverter:
        def __init__(self, conversion_factors):
            self.conversion_factors = conversion_factors
        def convert(self, value, from_unit, to_unit):
            if from_unit == to_unit:
                return value
            if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
                raise ValueError("Unit not found.")
            if (from_unit, to_unit) in self.conversion_factors:
                return value * self.conversion_factors[(from_unit, to_unit)]
            else:
                 raise NotImplementedError("Direct conversion not found. Chained conversion logic is complex without defined base system.")
    class ModularConverter:
        def __init__(self, factors):
            self.factors = factors
        def convert(self, value, from_unit, to_unit):
            if from_unit == to_unit:
                return value
            if (from_unit, to_unit) in self.factors:
                return value * self.factors[(from_unit, to_unit)]
            else:
                raise ValueError(f"Conversion factor from {from_unit} to {to_unit} not found.")
    pairwise_conversion = {
        ("meter", "cm"): 100.0,
        ("kg", "g"): 1000.0,
        ("mile", "km"): 1.60934,
        ("hour", "minute"): 60.0
    }
    modular_converter = ModularConverter(pairwise_conversion)
    print(f"Converting {value1} {from_unit1} to {to_unit1}:")
    try:
        result1 = modular_converter.convert(value1, from_unit1, to_unit1)
        print(f"Result: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    value2 = 2.5
    from_unit2 = "kg"
    to_unit2 = "g"
    print(f"Converting {value2} {from_unit2} to {to_unit2}:")
    try:
        result2 = modular_converter.convert(value2, from_unit2, to_unit2)
        print(f"Result: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    value3 = 10.0
    from_unit3 = "meter"
    to_unit3 = "kg"
    print(f"Converting {value3} {from_unit3} to {to_unit3}:")
    try:
        result3 = modular_converter.convert(value3, from_unit3, to_unit3)
        print(f"Result: {result3}")
    except ValueError as e:
        print(f"Error: {e}")