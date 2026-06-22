class UnitConverter:

    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors

    def convert(self, value, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f'Conversion to {target_unit} is not supported.')
        factor = self.conversion_factors[target_unit]
        return value * factor
if __name__ == '__main__':
    base_unit = 'meters'
    conversion_factors = {'centimeters': 100, 'millimeters': 1000, 'kilometers': 0.001, 'inches': 39.3701, 'feet': 3.28084, 'yards': 1.09361, 'miles': 0.000621371}
    converter = UnitConverter(base_unit, conversion_factors)
    value_in_meters = 5
    print(f"{value_in_meters} meters in centimeters: {converter.convert(value_in_meters, 'centimeters')}")
    print(f"{value_in_meters} meters in kilometers: {converter.convert(value_in_meters, 'kilometers')}")
    print(f"{value_in_meters} meters in inches: {converter.convert(value_in_meters, 'inches')}")