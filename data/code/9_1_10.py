class VolumeConverter:
    FACTOR_LITERS_TO_MILLILITERS = 1000.0
    FACTOR_MILLILITERS_TO_LITERS = 0.001
    FACTOR_CUBIC_METERS_TO_CUBIC_INCHES = 61023.744094732
    FACTOR_CUBIC_INCHES_TO_CUBIC_METERS = 1.6387064e-5

    def convert_liters_to_milliliters(self, liters):
        return liters * VolumeConverter.FACTOR_LITERS_TO_MILLILITERS

    def convert_milliliters_to_liters(self, milliliters):
        return milliliters * VolumeConverter.FACTOR_MILLILITERS_TO_LITERS

    def convert_cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * VolumeConverter.FACTOR_CUBIC_METERS_TO_CUBIC_INCHES

    def convert_cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches * VolumeConverter.FACTOR_CUBIC_INCHES_TO_CUBIC_METERS

if __name__ == '__main__':
    converter = VolumeConverter()
    liters_value = 2.5
    milliliters_result = converter.convert_liters_to_milliliters(liters_value)
    cubic_meters_value = 1.0
    cubic_inches_result = converter.convert_cubic_meters_to_cubic_inches(cubic_meters_value)
    print(liters_result)
    print(milliliters_result)
    print(cubic_inches_result)