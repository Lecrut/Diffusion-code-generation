class VolumeConverter:
    def __init__(self):
        self.liters_per_milliliter = 0.001
        self.milliliters_per_liter = 1000
        self.cubic_meters_per_cubic_inch = 1.63871e-5
        self.cubic_inches_per_cubic_meter = 61023.7

    def liters_to_milliliters(self, liters):
        return liters * self.milliliters_per_liter

    def milliliters_to_liters(self, milliliters):
        return milliliters * self.liters_per_milliliter

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * self.cubic_inches_per_cubic_meter

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches * self.cubic_meters_per_cubic_inch

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(500))
    print(converter.cubic_meters_to_cubic_inches(1))
    print(converter.cubic_inches_to_cubic_meters(61023.7))