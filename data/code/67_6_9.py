class VolumeConverter:
    def __init__(self):
        self._factor = 1000

    def to_milliliters(self, liters):
        return int(liters) * self._factor

    def to_liters(self, milliliters):
        return milliliters / self._factor

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.to_milliliters(2))
    print(converter.to_liters(5000))