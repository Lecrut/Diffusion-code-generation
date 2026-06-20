class VolumeConverter:
    LITERS_PER_MILLILITER = 0.001
    MILLILITERS_PER_LITER = 1000
    CUBIC_METERS_PER_CUBIC_INCH = 0.000016387064
    CUBIC_INCHES_PER_CUBIC_METER = 61023.7440947

    @staticmethod
    def liters_to_milliliters(liters):
        if liters < 0:
            raise ValueError("Volume cannot be negative")
        return liters * VolumeConverter.MILLILITERS_PER_LITER

    @staticmethod
    def milliliters_to_liters(milliliters):
        if milliliters < 0:
            raise ValueError("Volume cannot be negative")
        return milliliters * VolumeConverter.LITERS_PER_MILLILITER

    @staticmethod
    def cubic_meters_to_cubic_inches(cubic_meters):
        if cubic_meters < 0:
            raise ValueError("Volume cannot be negative")
        return cubic_meters * VolumeConverter.CUBIC_INCHES_PER_CUBIC_METER

    @staticmethod
    def cubic_inches_to_cubic_meters(cubic_inches):
        if cubic_inches < 0:
            raise ValueError("Volume cannot be negative")
        return cubic_inches * VolumeConverter.CUBIC_METERS_PER_CUBIC_INCH

if __name__ == '__main__':
    converter = VolumeConverter()

    sample_liters = 2.5
    sample_milliliters = 500
    sample_cubic_meters = 1.0
    sample_cubic_inches = 100

    liters_to_ml = converter.liters_to_milliliters(sample_liters)
    ml_to_liters = converter.milliliters_to_liters(sample_milliliters)
    cubic_m_to_cubic_in = converter.cubic_meters_to_cubic_inches(sample_cubic_meters)
    cubic_in_to_cubic_m = converter.cubic_inches_to_cubic_meters(sample_cubic_inches)

    print(liters_to_ml)
    print(ml_to_liters)
    print(cubic_m_to_cubic_in)
    print(cubic_in_to_cubic_m)