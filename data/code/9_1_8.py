class VolumeConverter:
    def __init__(self):
        self.liters_to_milliliters = 1000
        self.cubic_meters_to_cubic_inches = 61023.7441

    def liters_to_milliliters_conversion(self, liters):
        return liters * self.liters_to_milliliters

    def milliliters_to_liters_conversion(self, milliliters):
        return milliliters / self.liters_to_milliliters

    def cubic_meters_to_cubic_inches_conversion(self, cubic_meters):
        return cubic_meters * self.cubic_meters_to_cubic_inches

    def cubic_inches_to_cubic_meters_conversion(self, cubic_inches):
        return cubic_inches / self.cubic_meters_to_cubic_inches

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 5.5
    sample_cubic_meters = 2.0
    print(converter.liters_to_milliliters_conversion(sample_liters))
    print(converter.milliliters_to_liters_conversion(5500))
    print(converter.cubic_meters_to_cubic_inches_conversion(sample_cubic_meters))
    print(converter.cubic_inches_to_cubic_meters_conversion(122047.4882))