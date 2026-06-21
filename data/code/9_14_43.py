class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'pints': {'quarts': 0.5},
            'quarts': {'pints': 2.0}
        }

    def convert(self, volume, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
        return volume * self.conversion_factors[from_unit][to_unit]

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_pints1 = 10
    quarts1 = converter.convert(sample_pints1, 'pints', 'quarts')
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")
    sample_quarts2 = 5
    pints2 = converter.convert(sample_quarts2, 'quarts', 'pints')
    print(f"{sample_quarts2} quarts is equal to {pints2} pints")