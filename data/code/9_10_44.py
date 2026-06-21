class VolumeConverter:

    def __init__(self):
        self.liter_to_milliliter = 1000
        self.liter_to_gallon = 0.264172
        self.liter_to_quart = 1.05669
        self.liter_to_pint = 2.11338
        self.liter_to_cup = 4.22676
        self.liter_to_fluid_ounce = 33.814

    def liters_to_milliliters(self, liters):
        return liters * self.liter_to_milliliter

    def liters_to_gallons(self, liters):
        return liters * self.liter_to_gallon

    def liters_to_quarts(self, liters):
        return liters * self.liter_to_quart

    def liters_to_pints(self, liters):
        return liters * self.liter_to_pint

    def liters_to_cups(self, liters):
        return liters * self.liter_to_cup

    def liters_to_fluid_ounces(self, liters):
        return liters * self.liter_to_fluid_ounce

    def milliliters_to_liters(self, milliliters):
        return milliliters / self.liter_to_milliliter

    def gallons_to_liters(self, gallons):
        return gallons / self.liter_to_gallon

    def quarts_to_liters(self, quarts):
        return quarts / self.liter_to_quart

    def pints_to_liters(self, pints):
        return pints / self.liter_to_pint

    def cups_to_liters(self, cups):
        return cups / self.liter_to_cup

    def fluid_ounces_to_liters(self, fluid_ounces):
        return fluid_ounces / self.liter_to_fluid_ounce
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(1))
    print(converter.liters_to_gallons(1))
    print(converter.liters_to_quarts(1))
    print(converter.liters_to_pints(1))
    print(converter.liters_to_cups(1))
    print(converter.liters_to_fluid_ounces(1))
    print(converter.milliliters_to_liters(1000))
    print(converter.gallons_to_liters(0.264172))
    print(converter.quarts_to_liters(1.05669))
    print(converter.pints_to_liters(2.11338))
    print(converter.cups_to_liters(4.22676))
    print(converter.fluid_ounces_to_liters(33.814))