class VolumeConverter:
    def __init__(self):
        self.LITERS_PER_MILLILITER = 1000
        self.CUBIC_METERS_PER_CUBIC_INCH = 0.0000163871

    def liters_to_milliliters(self, liters):
        return liters * self.LITERS_PER_MILLILITER

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.LITERS_PER_MILLILITER

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters / self.CUBIC_METERS_PER_CUBIC_INCH

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches * self.CUBIC_METERS_PER_CUBIC_INCH

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 5
    sample_milliliters = 7500
    sample_cubic_meters = 2
    sample_cubic_inches = 1000

    result_liters_to_ml = converter.liters_to_milliliters(sample_liters)
    result_ml_to_liters = converter.milliliters_to_liters(sample_milliliters)
    result_cubic_m_to_in = converter.cubic_meters_to_cubic_inches(sample_cubic_meters)
    result_cubic_in_to_m = converter.cubic_inches_to_cubic_meters(sample_cubic_inches)

    print(result_liters_to_ml)
    print(result_ml_to_liters)
    print(result_cubic_m_to_in)
    print(result_cubic_in_to_m)