class VolumeConverter:
    def __init__(self, liters):
        self.liters = float(liters)

    def to_liters(self):
        return self.liters

    def to_milliliters(self):
        return self.liters * 1000.0

    def to_gallons(self):
        return self.liters / 3.785411784

    def to_quarts(self):
        return self.liters / 0.946352946

    def to_pints(self):
        return self.liters / 0.473176473

    def to_cups(self):
        return self.liters / 0.2365882365

    def to_fluid_ounces(self):
        return self.liters / 0.0295735295625

if __name__ == '__main__':
    converter = VolumeConverter(2.5)
    print(converter.to_liters())
    print(converter.to_milliliters())
    print(converter.to_gallons())
    print(converter.to_quarts())
    print(converter.to_pints())
    print(converter.to_cups())
    print(converter.to_fluid_ounces())