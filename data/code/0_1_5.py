class UnitConverter:
    M_TO_F = 3.28084
    M_TO_K = 0.001
    F_TO_M = 0.3048
    K_TO_M = 1000.0

    def meters_to_feet(self, meters):
        return meters * self.M_TO_F

    def meters_to_kilometers(self, meters):
        return meters * self.M_TO_K

    def feet_to_meters(self, feet):
        return feet * self.F_TO_M

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.K_TO_M

    def feet_to_kilometers(self, feet):
        meters = self.feet_to_meters(feet)
        return self.meters_to_kilometers(meters)

    def kilometers_to_feet(self, kilometers):
        meters = self.kilometers_to_meters(kilometers)
        return self.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(10))
    print(converter.feet_to_meters(32.8084))
    print(converter.meters_to_kilometers(1000))
    print(converter.kilometers_to_meters(1))
    print(converter.feet_to_kilometers(3280.84))
    print(converter.kilometers_to_feet(1))