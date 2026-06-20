class LengthConverter:
    METER_TO_FEET = 3.280839895013123
    FEET_TO_METER = 1.0 / METER_TO_FEET

    def __init__(self):
        self.conversion_factors = {
            ('m', 'm'): 1.0,
            ('ft', 'ft'): 1.0,
            ('m', 'ft'): self.METER_TO_FEET,
            ('ft', 'm'): self.FEET_TO_METER,
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in ('m', 'ft') or to_unit not in ('m', 'ft'):
            raise ValueError("Unsupported unit. Use 'm' for meters and 'ft' for feet.")
        factor = self.conversion_factors[(from_unit, to_unit)]
        return value * factor

if __name__ == '__main__':
    converter = LengthConverter()
    meters_to_feet = converter.convert(1.0, 'm', 'ft')
    print(meters_to_feet)
    feet_to_meters = converter.convert(1.0, 'ft', 'm')
    print(feet_to_meters)
    meters_to_meters = converter.convert(5.0, 'm', 'm')
    print(meters_to_meters)