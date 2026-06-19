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
    print(converter.meters_to_feet(10))
    print(converter.feet_to_meters(32.8084))
    print(converter.kilometers_to_meters(5))
    print(converter.meters_to_kilometers(1000))