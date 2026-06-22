class UnitConverter:
    FT_PER_M = 3.28084
    M_PER_KM = 1000.0
    FT_PER_KM = FT_PER_M * M_PER_KM

    def __init__(self):
        self._factors = {
            'm_to_ft': self.FT_PER_M,
            'km_to_m': self.M_PER_KM,
            'ft_to_m': 1.0 / self.FT_PER_M,
            'm_to_km': 1.0 / self.M_PER_KM,
            'ft_to_km': 1.0 / self.FT_PER_KM,
            'km_to_ft': self.FT_PER_KM,
        }

    def _apply(self, source_val, factor_key):
        return source_val * self._factors[factor_key]

    def convert_meters_to_feet(self, meters):
        return self._apply(meters, 'm_to_ft')

    def convert_kilometers_to_meters(self, kilometers):
        return self._apply(kilometers, 'km_to_m')

    def convert_feet_to_meters(self, feet):
        return self._apply(feet, 'ft_to_m')

    def convert_meters_to_kilometers(self, meters):
        return self._apply(meters, 'm_to_km')

    def convert_feet_to_kilometers(self, feet):
        return self._apply(feet, 'ft_to_km')

    def convert_kilometers_to_feet(self, kilometers):
        return self._apply(kilometers, 'km_to_ft')

if __name__ == '__main__':
    converter = UnitConverter()
    sample_meters = 100.0
    print(converter.convert_meters_to_feet(sample_meters))
    sample_kilometers = 5.0
    print(converter.convert_kilometers_to_meters(sample_kilometers))
    sample_feet = 328.084
    print(converter.convert_feet_to_meters(sample_feet))
    print(converter.convert_meters_to_kilometers(sample_meters))
    print(converter.convert_feet_to_kilometers(sample_feet))
    print(converter.convert_kilometers_to_feet(sample_kilometers))