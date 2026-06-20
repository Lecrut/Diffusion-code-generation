class VolumeConverter:
    LITER_TO_ML = 1000.0
    CUBIC_METER_TO_CUBIC_INCH = 61023.7441

    def liters_to_milliliters(self, liters):
        return liters * self.LITER_TO_ML

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.LITER_TO_ML

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * self.CUBIC_METER_TO_CUBIC_INCH

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / self.CUBIC_METER_TO_CUBIC_INCH

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(500))
    print(converter.cubic_meters_to_cubic_inches(1.0))
    print(converter.cubic_inches_to_cubic_meters(61023.7441))