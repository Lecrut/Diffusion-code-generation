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
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(1500))
    print(converter.cubic_meters_to_cubic_inches(1.0))
    print(converter.cubic_inches_to_cubic_meters(100000))