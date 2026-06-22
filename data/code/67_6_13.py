class VolumeConverter:
    LITERS_TO_MILLILITERS_FACTOR = 1000

    def __init__(self, liters: int):
        self._liters = liters

    def to_milliliters(self) -> int:
        if self._liters < 0:
            raise ValueError("Volume cannot be negative")
        return self._liters * self.LITERS_TO_MILLILITERS_FACTOR

if __name__ == '__main__':
    converter = VolumeConverter(42)
    print(converter.to_milliliters())