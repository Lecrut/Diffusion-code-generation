class VolumeConverter:
    _MILLILITERS_PER_LITER = 1000

    def convert(self, liters: int) -> int:
        return liters * self._MILLILITERS_PER_LITER

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(42))