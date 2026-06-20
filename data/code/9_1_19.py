class VolumeConverter:
    LITERS_IN_CUBIC_METER = 1000
    MILLILITERS_IN_LITER = 1000
    INCHES_IN_METER = 39.3701

    def liters_to_milliliters(self, liters):
        return liters * self.MILLILITERS_IN_LITER

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.MILLILITERS_IN_LITER

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        inches_per_meter = self.INCHES_IN_METER
        return cubic_meters * (inches_per_meter ** 3)

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        inches_per_meter = self.INCHES_IN_METER
        return cubic_inches / (inches_per_meter ** 3)

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(5))
    print(converter.cubic_meters_to_cubic_inches(2))