class VolumeConverter:
    MILLILITERS_PER_LITER = 1000

    def __init__(self, liters: float) -> None:
        self.liters = liters

    def to_milliliters(self) -> float:
        return self.liters * self.MILLILITERS_PER_LITER

if __name__ == '__main__':
    converter_one = VolumeConverter(5.0)
    print(converter_one.to_milliliters())
    converter_two = VolumeConverter(0.025)
    print(converter_two.to_milliliters())
    converter_three = VolumeConverter(12.75)
    print(converter_three.to_milliliters())