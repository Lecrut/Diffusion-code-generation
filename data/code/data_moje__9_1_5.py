class VolumeConverter:
    def liters_to_milliliters(self, liters):
        return liters * 1000

    def milliliters_to_liters(self, milliliters):
        return milliliters / 1000

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * 61023.7441

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / 61023.7441

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(5))
    print(converter.milliliters_to_liters(2500))
    print(converter.cubic_meters_to_cubic_inches(2))
    print(converter.cubic_inches_to_cubic_meters(122047.4882))