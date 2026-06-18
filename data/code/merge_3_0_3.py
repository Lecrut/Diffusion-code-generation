class UnitConverter:
    METER_TO_FOOT = 3.28084
    FOOT_TO_METER = 1 / 3.28084
    METER_TO_KILOMETER = 1 / 1000
    KILOMETER_TO_METER = 1000
    def meters_to_feet(self, meters):
        return meters * self.METER_TO_FOOT
    def feet_to_meters(self, feet):
        return feet * self.FOOT_TO_METER
    def meters_to_kilometers(self, meters):
        return meters * self.METER_TO_KILOMETER
    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETER_TO_METER
if __name__ == '__main__':
    converter = UnitConverter()
    meters_value = 10
    feet_value = 32.8084
    kilometers_value = 5
    meters_to_feet_result = converter.meters_to_feet(meters_value)
    feet_to_meters_result = converter.feet_to_meters(feet_value)
    meters_to_kilometers_result = converter.meters_to_kilometers(meters_value)
    kilometers_to_meters_result = converter.kilometers_to_meters(kilometers_value)
    print(f"Conversion of {meters_value} meters to feet: {meters_to_feet_result}")
    print(f"Conversion of {feet_value} feet to meters: {feet_to_meters_result}")
    print(f"Conversion of {meters_value} meters to kilometers: {meters_to_kilometers_result}")
    print(f"Conversion of {kilometers_value} kilometers to meters: {kilometers_to_meters_result}")