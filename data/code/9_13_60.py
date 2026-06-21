class VolumeUnitConverter:
    UNIT_CONVERSIONS = {
        'gallons_to_liters': 3.78541,
    }

    def convert(self, value, from_unit, to_unit):
        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported")
        return value * self.UNIT_CONVERSIONS[conversion_key]

if __name__ == '__main__':
    sample_gallons = 8.0
    converter = VolumeUnitConverter()
    converted_liters = converter.convert(sample_gallons, 'gallons', 'liters')
    print(converted_liters)