class VolumeConverter:

    def __init__(self):
        self.liters_to_milliliters = 1000
        self.milliliters_to_liters = 1 / 1000
        self.gallons_to_liters = 3.78541
        self.liters_to_gallons = 1 / 3.78541
        self.quarts_to_liters = 0.946353
        self.liters_to_quarts = 1 / 0.946353
        self.pints_to_liters = 0.473176
        self.liters_to_pints = 1 / 0.473176
        self.cups_to_liters = 0.236588
        self.liters_to_cups = 1 / 0.236588
        self.fluid_ounces_to_liters = 0.0295735
        self.liters_to_fluid_ounces = 1 / 0.0295735

    def liters_to_milliliters(self, liters):
        return liters * self.liters_to_milliliters

    def milliliters_to_liters(self, milliliters):
        return milliliters * self.milliliters_to_liters

    def gallons_to_liters(self, gallons):
        return gallons * self.gallons_to_liters

    def liters_to_gallons(self, liters):
        return liters * self.liters_to_gallons

    def quarts_to_liters(self, quarts):
        return quarts * self.quarts_to_liters

    def liters_to_quarts(self, liters):
        return liters * self.liters_to_quarts

    def pints_to_liters(self, pints):
        return pints * self.pints_to_liters

    def liters_to_pints(self, liters):
        return liters * self.liters_to_pints

    def cups_to_liters(self, cups):
        return cups * self.cups_to_liters

    def liters_to_cups(self, liters):
        return liters * self.liters_to_cups

    def fluid_ounces_to_liters(self, fluid_ounces):
        return fluid_ounces * self.fluid_ounces_to_liters

    def liters_to_fluid_ounces(self, liters):
        return liters * self.liters_to_fluid_ounces
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(1500))
    print(converter.gallons_to_liters(1))
    print(converter.liters_to_gallons(2))
    print(converter.quarts_to_liters(4))
    print(converter.liters_to_quarts(1))
    print(converter.pints_to_liters(8))
    print(converter.liters_to_pints(2))
    print(converter.cups_to_liters(16))
    print(converter.liters_to_cups(1))
    print(converter.fluid_ounces_to_liters(32))
    print(converter.liters_to_fluid_ounces(1))