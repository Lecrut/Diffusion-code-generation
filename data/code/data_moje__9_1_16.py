class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    MILLILITERS_TO_LITERS = 0.001
    CUBIC_METERS_TO_CUBIC_INCHES = 61023.744094732
    CUBIC_INCHES_TO_CUBIC_METERS = 1 / 61023.744094732

    def convert_liters_to_milliliters(self, liters):
        return liters * self.LITERS_TO_MILLILITERS

    def convert_milliliters_to_liters(self, milliliters):
        return milliliters * self.MILLILITERS_TO_LITERS

    def convert_cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * self.CUBIC_METERS_TO_CUBIC_INCHES

    def convert_cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches * self.CUBIC_INCHES_TO_CUBIC_METERS

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert_liters_to_milliliters(2.5))
    print(converter.convert_milliliters_to_liters(500))
    print(converter.convert_cubic_meters_to_cubic_inches(1))
    print(converter.convert_cubic_inches_to_cubic_meters(61023.744094732))