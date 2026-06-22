class VolumeConverter:

    def liters_to_milliliters(self, liters):
        return liters * 1000

    def milliliters_to_liters(self, milliliters):
        return milliliters / 1000

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * 61023.7440947

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / 61023.7440947
if __name__ == '__main__':
    converter = VolumeConverter()
    liters_value = 5.0
    milliliters_value = 2000.0
    cubic_meters_value = 1.0
    cubic_inches_value = 1000.0
    print(converter.liters_to_milliliters(liters_value))
    print(converter.milliliters_to_liters(milliliters_value))
    print(converter.cubic_meters_to_cubic_inches(cubic_meters_value))
    print(converter.cubic_inches_to_cubic_meters(cubic_inches_value))