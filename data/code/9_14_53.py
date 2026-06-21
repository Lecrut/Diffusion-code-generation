class VolumeConverter:
    PINTS_TO_QUARTS = 0.5

    @staticmethod
    def convert_pints_to_quarts(pints):
        if pints < 0:
            raise ValueError("Volume cannot be negative")
        return pints * VolumeConverter.PINTS_TO_QUARTS

if __name__ == '__main__':
    sample_pints1 = 10
    quarts1 = VolumeConverter.convert_pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")
    
    sample_pints2 = 25
    quarts2 = VolumeConverter.convert_pints_to_quarts(sample_pints2)
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")