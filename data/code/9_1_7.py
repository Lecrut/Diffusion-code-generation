class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    MILLILITERS_TO_LITERS = 0.001
    CUBIC_METERS_TO_CUBIC_INCHES = 61023.7441
    CUBIC_INCHES_TO_CUBIC_METERS = 1.6387064e-5

    def liters_to_milliliters(self, liters):
        return liters * self.LITERS_TO_MILLILITERS

    def milliliters_to_liters(self, milliliters):
        return milliliters * self.MILLILITERS_TO_LITERS

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * self.CUBIC_METERS_TO_CUBIC_INCHES

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches * self.CUBIC_INCHES_TO_CUBIC_METERS

if __name__ == '__main__':
    converter = VolumeConverter()
    
    liters_value = 2.5
    ml_result = converter.liters_to_milliliters(liters_value)
    print(f"{liters_value} liters is {ml_result} milliliters")
    
    cubic_meters_value = 1.0
    cubic_inches_result = converter.cubic_meters_to_cubic_inches(cubic_meters_value)
    print(f"{cubic_meters_value} cubic meters is {cubic_inches_result} cubic inches")