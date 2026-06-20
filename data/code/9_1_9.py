class VolumeConverter:
    LITERS_TO_ML = 1000
    ML_TO_LITERS = 0.001
    CUBIC_METERS_TO_INCHES = 61023.744094732
    INCHES_TO_CUBIC_METERS = 1 / 61023.744094732

    def liters_to_milliliters(self, liters):
        if liters < 0:
            raise ValueError("Volume cannot be negative")
        return liters * self.LITERS_TO_ML

    def milliliters_to_liters(self, milliliters):
        if milliliters < 0:
            raise ValueError("Volume cannot be negative")
        return milliliters * self.ML_TO_LITERS

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        if cubic_meters < 0:
            raise ValueError("Volume cannot be negative")
        return cubic_meters * self.CUBIC_METERS_TO_INCHES

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        if cubic_inches < 0:
            raise ValueError("Volume cannot be negative")
        return cubic_inches * self.INCHES_TO_CUBIC_METERS

if __name__ == '__main__':
    converter = VolumeConverter()

    liters_value = 2.5
    ml_result = converter.liters_to_milliliters(liters_value)
    print(f"{liters_value} liters is {ml_result} milliliters")

    cubic_meters_value = 1.0
    cubic_inches_result = converter.cubic_meters_to_cubic_inches(cubic_meters_value)
    print(f"{cubic_meters_value} cubic meters is {cubic_inches_result} cubic inches")

    ml_value = 500
    liters_result = converter.milliliters_to_liters(ml_value)
    print(f"{ml_value} milliliters is {liters_result} liters")

    cubic_inches_value = 100
    cubic_meters_result = converter.cubic_inches_to_cubic_meters(cubic_inches_value)
    print(f"{cubic_inches_value} cubic inches is {cubic_meters_result} cubic meters")