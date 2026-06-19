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
    feet_value = 30
    kilometers_value = 5
    print(f'{meters_value} meters is {converter.meters_to_feet(meters_value)} feet')
    print(f'{feet_value} feet is {converter.feet_to_meters(feet_value)} meters')
    print(f'{kilometers_value} kilometers is {converter.kilometers_to_meters(kilometers_value)} meters')
    print(f'{meters_value} meters is {converter.meters_to_kilometers(meters_value)} kilometers')