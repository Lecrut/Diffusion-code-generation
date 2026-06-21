class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {
            'meters': 1.0,
            'centimeters': 100.0,
            'millimeters': 1000.0,
            'kilometers': 0.001,
            'inches': 39.3701,
            'feet': 3.28084,
            'yards': 1.09361,
            'miles': 0.000621371
        }

    def convert(self, value, target_unit):
        if self.base_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported base unit: {self.base_unit}")
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        base_value = value * self.conversion_factors[self.base_unit]
        converted_value = base_value / self.conversion_factors[target_unit]
        return converted_value

if __name__ == '__main__':
    converter = UnitConverter('meters')
    sample_values = [
        (1, 'centimeters'),
        (2.5, 'feet'),
        (1000, 'kilometers'),
        (39.3701, 'inches')
    ]

    for value, target_unit in sample_values:
        result = converter.convert(value, target_unit)
        print(f"{value} {converter.base_unit} is {result} {target_unit}")