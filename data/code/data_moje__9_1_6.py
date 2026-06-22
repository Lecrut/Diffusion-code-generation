class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000

    @staticmethod
    def milliliters_to_liters(milliliters):
        return milliliters / 1000

    @staticmethod
    def cubic_meters_to_cubic_inches(cubic_meters):
        conversion_factor = 61023.7440947323
        return cubic_meters * conversion_factor

    @staticmethod
    def cubic_inches_to_cubic_meters(cubic_inches):
        conversion_factor = 61023.7440947323
        return cubic_inches / conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(500))
    print(converter.cubic_meters_to_cubic_inches(1.0))
    print(converter.cubic_inches_to_cubic_meters(1000))