class VolumeConverter:
    LITERS_TO_ML = 1000.0
    CUBIC_METERS_TO_INCHES = 61023.744095

    def liters_to_milliliters(self, liters):
        return liters * self.LITERS_TO_ML

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.LITERS_TO_ML

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * self.CUBIC_METERS_TO_INCHES

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / self.CUBIC_METERS_TO_INCHES

if __name__ == '__main__':
    converter = VolumeConverter()
    liters = 2.5
    milliliters = converter.liters_to_milliliters(liters)
    print(milliliters)

    cubic_meters = 1.0
    cubic_inches = converter.cubic_meters_to_cubic_inches(cubic_meters)
    print(cubic_inches)

    ml_back = converter.milliliters_to_liters(5000)
    print(ml_back)

    ci_back = converter.cubic_inches_to_cubic_meters(61023.744095)
    print(ci_back)