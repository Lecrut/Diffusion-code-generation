class VolumeConverter:
    PINTS_TO_QUARTS_FACTOR = 0.5

    def convert_pints_to_quarts(self, pints):
        if not isinstance(pints, (int, float)):
            raise ValueError("Volume must be a number")
        if pints < 0:
            raise ValueError("Volume cannot be negative")
        return pints * self.PINTS_TO_QUARTS_FACTOR

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_pints1 = 4
    quarts1 = converter.convert_pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")
    sample_pints2 = 10
    quarts2 = converter.convert_pints_to_quarts(sample_pints2)
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")