class VolumeConverter:
    PINTS_TO_QUARTS_RATIO = 0.5

    def __init__(self):
        self.conversion_factors = {
            'pints_to_quarts': self.PINTS_TO_QUARTS_RATIO,
            'quarts_to_pints': 2.0
        }

    def convert(self, volume, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit conversion from {from_unit} to {to_unit}")
        key = f"{from_unit}_to_{to_unit}"
        if key not in self.conversion_factors:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not directly supported")
        return volume * self.conversion_factors[key]

    def pints_to_quarts(self, pints):
        if pints < 0:
            raise ValueError("Volume cannot be negative")
        return self.convert(pints, 'pints', 'quarts')

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_pints1 = 6
    quarts1 = converter.pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")
    sample_pints2 = 10
    quarts2 = converter.convert(sample_pints2, 'pints', 'quarts')
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")