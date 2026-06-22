class VolumeConverter:
    FACTORS = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
        'gallon_us': 3.78541,
        'gallon_uk': 4.54609,
        'quart_us': 0.946353,
        'pint_us': 0.473176,
        'cup_us': 0.236588,
        'fluid_ounce_us': 0.0295735,
        'tablespoon_us': 0.0147868,
        'teaspoon_us': 0.00492892,
        'barrel_us': 119.24,
        'imperial_gallon': 4.54609,
    }

    def to_base(self, volume, unit):
        normalized_unit = unit.lower().replace(' ', '_').replace('-', '_')
        if normalized_unit not in self.FACTORS:
            raise ValueError(f"Unsupported unit: {unit}")
        return volume * self.FACTORS[normalized_unit]

    def from_base(self, base_volume, unit):
        normalized_unit = unit.lower().replace(' ', '_').replace('-', '_')
        if normalized_unit not in self.FACTORS:
            raise ValueError(f"Unsupported unit: {unit}")
        return base_volume / self.FACTORS[normalized_unit]

    def convert(self, volume, from_unit, to_unit):
        base_volume = self.to_base(volume, from_unit)
        return self.from_base(base_volume, to_unit)

    def get_supported_units(self):
        return list(self.FACTORS.keys())

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_volume = 1
    sample_from = 'gallon_us'
    sample_to = 'liter'
    result = converter.convert(sample_volume, sample_from, sample_to)
    print(result)
    
    sample_volume2 = 1000
    sample_from2 = 'milliliter'
    sample_to2 = 'cup_us'
    result2 = converter.convert(sample_volume2, sample_from2, sample_to2)
    print(result2)
    
    sample_volume3 = 1
    sample_from3 = 'cubic_meter'
    sample_to3 = 'gallon_uk'
    result3 = converter.convert(sample_volume3, sample_from3, sample_to3)
    print(result3)