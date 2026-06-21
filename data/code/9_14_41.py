class VolumeUnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'pints_to_quarts': 0.5,
            'quarts_to_pints': 2.0
        }

    def convert_pints_to_quarts(self, pints):
        if pints < 0:
            raise ValueError("Volume cannot be negative")
        return pints * self.conversion_factors['pints_to_quarts']

if __name__ == '__main__':
    converter = VolumeUnitConverter()
    sample_pints1 = 8
    quarts1 = converter.convert_pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")

    sample_pints2 = 15
    quarts2 = converter.convert_pints_to_quarts(sample_pints2)
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")