class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000.0
    CUBIC_METERS_TO_CUBIC_INCHES = 61023.7440947323

    @classmethod
    def liters_to_milliliters(cls, liters):
        return liters * cls.LITERS_TO_MILLILITERS

    @classmethod
    def milliliters_to_liters(cls, milliliters):
        return milliliters / cls.LITERS_TO_MILLILITERS

    @classmethod
    def cubic_meters_to_cubic_inches(cls, cubic_meters):
        return cubic_meters * cls.CUBIC_METERS_TO_CUBIC_INCHES

    @classmethod
    def cubic_inches_to_cubic_meters(cls, cubic_inches):
        return cubic_inches / cls.CUBIC_METERS_TO_CUBIC_INCHES

if __name__ == '__main__':
    converter = VolumeConverter()

    liters = 2.5
    milliliters = converter.liters_to_milliliters(liters)
    print(milliliters)

    original_liters = converter.milliliters_to_liters(milliliters)
    print(original_liters)

    cubic_meters = 1.0
    cubic_inches = converter.cubic_meters_to_cubic_inches(cubic_meters)
    print(cubic_inches)

    original_cubic_meters = converter.cubic_inches_to_cubic_meters(cubic_inches)
    print(original_cubic_meters)