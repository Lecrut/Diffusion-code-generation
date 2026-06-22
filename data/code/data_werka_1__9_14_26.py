class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    LITERS_TO_GALLONS = 0.264172
    GALLONS_TO_QUARTS = 4
    QUARTS_TO_PINTS = 2
    PINTS_TO_CUPS = 2
    CUPS_TO_FLUID_OUNCES = 8

    def liters_to_milliliters(self, liters):
        return liters * self.LITERS_TO_MILLILITERS

    def liters_to_gallons(self, liters):
        return liters * self.LITERS_TO_GALLONS

    def gallons_to_quarts(self, gallons):
        return gallons * self.GALLONS_TO_QUARTS

    def quarts_to_pints(self, quarts):
        return quarts * self.QUARTS_TO_PINTS

    def pints_to_cups(self, pints):
        return pints * self.PINTS_TO_CUPS

    def cups_to_fluid_ounces(self, cups):
        return cups * self.CUPS_TO_FLUID_OUNCES

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.LITERS_TO_MILLILITERS

    def gallons_to_liters(self, gallons):
        return gallons / self.LITERS_TO_GALLONS

    def quarts_to_gallons(self, quarts):
        return quarts / self.GALLONS_TO_QUARTS

    def pints_to_quarts(self, pints):
        return pints / self.QUARTS_TO_PINTS

    def cups_to_pints(self, cups):
        return cups / self.PINTS_TO_CUPS

    def fluid_ounces_to_cups(self, fluid_ounces):
        return fluid_ounces / self.CUPS_TO_FLUID_OUNCES
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2))
    print(converter.gallons_to_liters(1))
    print(converter.pints_to_cups(3))
    print(converter.fluid_ounces_to_cups(48))