class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_LITERS = 3.78541
    QUARTS_TO_LITERS = 0.946353
    PINTS_TO_LITERS = 0.473176
    CUPS_TO_LITERS = 0.236588
    FLUID_OUNCES_TO_LITERS = 0.0295735

    def liters_to_milliliters(self, liters):
        return liters * self.LITERS_TO_MILLILITERS

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.LITERS_TO_MILLILITERS

    def gallons_to_liters(self, gallons):
        return gallons * self.GALLONS_TO_LITERS

    def liters_to_gallons(self, liters):
        return liters / self.GALLONS_TO_LITERS

    def quarts_to_liters(self, quarts):
        return quarts * self.QUARTS_TO_LITERS

    def liters_to_quarts(self, liters):
        return liters / self.QUARTS_TO_LITERS

    def pints_to_liters(self, pints):
        return pints * self.PINTS_TO_LITERS

    def liters_to_pints(self, liters):
        return liters / self.PINTS_TO_LITERS

    def cups_to_liters(self, cups):
        return cups * self.CUPS_TO_LITERS

    def liters_to_cups(self, liters):
        return liters / self.CUPS_TO_LITERS

    def fluid_ounces_to_liters(self, fluid_ounces):
        return fluid_ounces * self.FLUID_OUNCES_TO_LITERS

    def liters_to_fluid_ounces(self, liters):
        return liters / self.FLUID_OUNCES_TO_LITERS
if __name__ == '__main__':
    converter = VolumeConverter()
    print('1 liter to milliliters:', converter.liters_to_milliliters(1))
    print('500 milliliters to liters:', converter.milliliters_to_liters(500))
    print('2 gallons to liters:', converter.gallons_to_liters(2))
    print('10 liters to gallons:', converter.liters_to_gallons(10))
    print('4 quarts to liters:', converter.quarts_to_liters(4))
    print('8 liters to quarts:', converter.liters_to_quarts(8))
    print('6 pints to liters:', converter.pints_to_liters(6))
    print('3 liters to pints:', converter.liters_to_pints(3))
    print('12 cups to liters:', converter.cups_to_liters(12))
    print('5 liters to cups:', converter.liters_to_cups(5))
    print('32 fluid ounces to liters:', converter.fluid_ounces_to_liters(32))
    print('1 liter to fluid ounces:', converter.liters_to_fluid_ounces(1))