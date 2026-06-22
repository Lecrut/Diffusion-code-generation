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
    meters = 10
    feet = converter.meters_to_feet(meters)
    print(f'{meters} meters is {feet} feet')
    kilometers = 5
    meters_from_km = converter.kilometers_to_meters(kilometers)
    print(f'{kilometers} kilometers is {meters_from_km} meters')