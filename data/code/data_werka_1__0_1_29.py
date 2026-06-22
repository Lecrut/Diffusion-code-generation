class UnitConverter:
    M_TO_FEET = 3.28084
    KM_TO_M = 1000

    def meters_to_feet(self, meters):
        return meters * self.M_TO_FEET

    def feet_to_meters(self, feet):
        return feet / self.M_TO_FEET

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KM_TO_M

    def meters_to_kilometers(self, meters):
        return meters / self.KM_TO_M
if __name__ == '__main__':
    converter = UnitConverter()
    meters_value = 10
    feet_value = converter.meters_to_feet(meters_value)
    print(f'{meters_value} meters is {feet_value} feet')
    kilometers_value = 5
    meters_value_from_km = converter.kilometers_to_meters(kilometers_value)
    print(f'{kilometers_value} kilometers is {meters_value_from_km} meters')