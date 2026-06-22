class UnitConverter:
    METER_TO_FOOT = 3.28084
    METER_TO_KILOMETER = 0.001
    FOOT_TO_METER = 1 / METER_TO_FOOT
    KILOMETER_TO_METER = 1000.0

    def meters_to_feet(self, value):
        return value * self.METER_TO_FOOT

    def meters_to_kilometers(self, value):
        return value * self.METER_TO_KILOMETER

    def feet_to_meters(self, value):
        return value * self.FOOT_TO_METER

    def kilometers_to_meters(self, value):
        return value * self.KILOMETER_TO_METER

    def feet_to_kilometers(self, value):
        return value * self.FOOT_TO_METER * self.METER_TO_KILOMETER

    def kilometers_to_feet(self, value):
        return value * self.KILOMETER_TO_METER * self.METER_TO_FOOT

if __name__ == '__main__':
    converter = UnitConverter()
    result_feet = converter.meters_to_feet(10)
    print(result_feet)
    result_km = converter.kilometers_to_feet(2)
    print(result_km)