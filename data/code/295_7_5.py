class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        try:
            value_in_base = value
            if from_unit != 'base':
                value_in_base *= self.conversion_factors[from_unit]
            if to_unit != 'base':
                value_in_base /= self.conversion_factors[to_unit]
            return value_in_base
        except KeyError:
            raise ValueError("Conversion failed due to missing factor.")
class System:
    def __init__(self, config):
        self.converter = UnitConverter(config)
    def convert_units(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        try:
            value_in_base = value
            if from_unit != 'base':
                value_in_base *= self.converter.conversion_factors[from_unit]
            if to_unit != 'base':
                value_in_base /= self.converter.conversion_factors[to_unit]
            return value_in_base
        except KeyError as e:
            raise ValueError(f"Error during conversion: {e}")
if __name__ == '__main__':
    conversion_config = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'gram': 0.001,
        'kilogram': 1000.0,
    }
    system = System(conversion_config)
    value = 5.0
    from_unit = 'kilometer'
    to_unit = 'meter'
    try:
        result = system.convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
        value2 = 10.0
        from_unit2 = 'mile'
        to_unit2 = 'kilometer'
        result2 = system.convert_units(value2, from_unit2, to_unit2)
        print(f"{value2} {from_unit2} is equal to {result2} {to_unit2}")
    except ValueError as e:
        print(f"Error: {e}")