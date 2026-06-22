class DistanceConverter:
    MILES_TO_KM = 1.60934
    MILES_TO_METERS = 1609.34
    KM_TO_METERS = 1000.0
    METERS_TO_KM = 0.001
    METERS_TO_MILES = 1 / 1609.34
    KM_TO_MILES = 1 / 1.60934

    def __init__(self):
        self.conversion_matrix = {
            ('miles', 'miles'): 1,
            ('miles', 'kilometers'): self.MILES_TO_KM,
            ('miles', 'meters'): self.MILES_TO_METERS,
            ('kilometers', 'miles'): self.KM_TO_MILES,
            ('kilometers', 'kilometers'): 1,
            ('kilometers', 'meters'): self.KM_TO_METERS,
            ('meters', 'miles'): self.METERS_TO_MILES,
            ('meters', 'kilometers'): self.METERS_TO_KM,
            ('meters', 'meters'): 1,
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in ('miles', 'kilometers', 'meters'):
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in ('miles', 'kilometers', 'meters'):
            raise ValueError(f"Unsupported unit: {to_unit}")
        factor = self.conversion_matrix[(from_unit, to_unit)]
        return value * factor

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'miles', 'kilometers'))
    print(converter.convert(1000, 'meters', 'miles'))
    print(converter.convert(5, 'kilometers', 'meters'))