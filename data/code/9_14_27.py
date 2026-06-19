class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_LITERS = 3.78541
    QUARTS_TO_LITERS = GALLONS_TO_LITERS / 4
    PINTS_TO_LITERS = QUARTS_TO_LITERS / 2
    CUPS_TO_LITERS = PINTS_TO_LITERS / 2
    FLUID_OUNCES_TO_LITERS = CUPS_TO_LITERS / 8

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
    sample_liters = 2.5
    print("Liters to Milliliters:", converter.liters_to_milliliters(sample_liters))
    print("Milliliters to Liters:", converter.milliliters_to_liters(2500))
    print("Gallons to Liters:", converter.gallons_to_liters(1))
    print("Liters to Gallons:", converter.liters_to_gallons(converter.GALLONS_TO_LITERS))
    print("Quarts to Liters:", converter.quarts_to_liters(2))
    print("Liters to Quarts:", converter.liters_to_quarts(converter.QUARTS_TO_LITERS * 2))
    print("Pints to Liters:", converter.pints_to_liters(4))
    print("Liters to Pints:", converter.liters_to_pints(converter.PINTS_TO_LITERS * 4))
    print("Cups to Liters:", converter.cups_to_liters(8))
    print("Liters to Cups:", converter.liters_to_cups(converter.CUPS_TO_LITERS * 8))
    print("Fluid Ounces to Liters:", converter.fluid_ounces_to_liters(32))
    print("Liters to Fluid Ounces:", converter.liters_to_fluid_ounces(converter.FLUID_OUNCES_TO_LITERS * 32))