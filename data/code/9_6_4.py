CONVERSION_FACTORS = {
    ('liter', 'milliliter'): 1000.0,
    ('liter', 'gallon'): 0.264172,
    ('liter', 'cubic_meter'): 0.001,
    ('milliliter', 'liter'): 0.001,
    ('milliliter', 'gallon'): 0.000264172,
    ('milliliter', 'cubic_meter'): 0.000001,
    ('gallon', 'liter'): 3.78541,
    ('gallon', 'milliliter'): 3785.41,
    ('gallon', 'cubic_meter'): 0.00378541,
    ('cubic_meter', 'liter'): 1000.0,
    ('cubic_meter', 'milliliter'): 1000000.0,
    ('cubic_meter', 'gallon'): 264.172,
}

class VolumeConverter:
    def __init__(self, conversion_dict):
        self.factors = conversion_dict

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        factor = self.factors.get((from_unit, to_unit))
        if factor is None:
            raise ValueError(f"No conversion factor found from {from_unit} to {to_unit}")
        return value * factor

if __name__ == '__main__':
    converter = VolumeConverter(CONVERSION_FACTORS)
    print(converter.convert(1.0, 'liter', 'milliliter'))
    print(converter.convert(1.0, 'cubic_meter', 'gallon'))
    print(converter.convert(5.0, 'gallon', 'liter'))