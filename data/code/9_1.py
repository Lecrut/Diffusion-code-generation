class VolumeConverter:
    LITERS_TO_ML = 1000.0
    ML_TO_LITERS = 0.001
    CUBIC_METERS_TO_CUBIC_INCHES = 61023.7440947
    CUBIC_INCHES_TO_CUBIC_METERS = 1 / 61023.7440947

    @staticmethod
    def liters_to_milliliters(liters):
        return liters * VolumeConverter.LITERS_TO_ML

    @staticmethod
    def milliliters_to_liters(milliliters):
        return milliliters * VolumeConverter.ML_TO_LITERS

    @staticmethod
    def cubic_meters_to_cubic_inches(cubic_meters):
        return cubic_meters * VolumeConverter.CUBIC_METERS_TO_CUBIC_INCHES

    @staticmethod
    def cubic_inches_to_cubic_meters(cubic_inches):
        return cubic_inches * VolumeConverter.CUBIC_INCHES_TO_CUBIC_METERS

if __name__ == '__main__':
    converter = VolumeConverter()

    liters_input = 2.5
    ml_result = converter.liters_to_milliliters(liters_input)
    print(f"{liters_input} liters is {ml_result} milliliters")

    ml_input = 500
    liters_result = converter.milliliters_to_liters(ml_input)
    print(f"{ml_input} milliliters is {liters_result} liters")

    cubic_meters_input = 1.0
    cubic_inches_result = converter.cubic_meters_to_cubic_inches(cubic_meters_input)
    print(f"{cubic_meters_input} cubic meters is {cubic_inches_result} cubic inches")

    cubic_inches_input = 100
    cubic_meters_result = converter.cubic_inches_to_cubic_meters(cubic_inches_input)
    print(f"{cubic_inches_input} cubic inches is {cubic_meters_result} cubic meters")