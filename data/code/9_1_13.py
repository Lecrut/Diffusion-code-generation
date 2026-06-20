class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000.0
    CUBIC_METERS_TO_CUBIC_INCHES = 61023.7440947323

    @staticmethod
    def liters_to_milliliters(liters):
        return liters * VolumeConverter.LITERS_TO_MILLILITERS

    @staticmethod
    def milliliters_to_liters(milliliters):
        return milliliters / VolumeConverter.LITERS_TO_MILLILITERS

    @staticmethod
    def cubic_meters_to_cubic_inches(cubic_meters):
        return cubic_meters * VolumeConverter.CUBIC_METERS_TO_CUBIC_INCHES

    @staticmethod
    def cubic_inches_to_cubic_meters(cubic_inches):
        return cubic_inches / VolumeConverter.CUBIC_METERS_TO_CUBIC_INCHES

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(1))
    print(converter.milliliters_to_liters(1000))
    print(converter.cubic_meters_to_cubic_inches(1))
    print(converter.cubic_inches_to_cubic_meters(61023.7440947323))