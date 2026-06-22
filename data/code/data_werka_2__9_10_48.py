class VolumeConverter:

    def __init__(self):
        self.LITERS_TO_MILLILITERS = 1000
        self.GALLONS_TO_LITERS = 3.78541
        self.QUARTS_TO_LITERS = 0.946353
        self.PINTS_TO_LITERS = 0.473176
        self.CUPS_TO_LITERS = 0.236588
        self.FLUID_OUNCES_TO_LITERS = 0.0295735

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
    sample_milliliters = 1500
    sample_gallons = 1.0
    sample_quarts = 3.0
    sample_pints = 6.0
    sample_cups = 8.0
    sample_fluid_ounces = 32.0
    print(f'{sample_liters} liters to milliliters: {converter.liters_to_milliliters(sample_liters)}')
    print(f'{sample_milliliters} milliliters to liters: {converter.milliliters_to_liters(sample_milliliters)}')
    print(f'{sample_gallons} gallons to liters: {converter.gallons_to_liters(sample_gallons)}')
    print(f'{sample_liters} liters to gallons: {converter.liters_to_gallons(sample_liters)}')
    print(f'{sample_quarts} quarts to liters: {converter.quarts_to_liters(sample_quarts)}')
    print(f'{sample_liters} liters to quarts: {converter.liters_to_quarts(sample_liters)}')
    print(f'{sample_pints} pints to liters: {converter.pints_to_liters(sample_pints)}')
    print(f'{sample_liters} liters to pints: {converter.liters_to_pints(sample_liters)}')
    print(f'{sample_cups} cups to liters: {converter.cups_to_liters(sample_cups)}')
    print(f'{sample_liters} liters to cups: {converter.liters_to_cups(sample_liters)}')
    print(f'{sample_fluid_ounces} fluid ounces to liters: {converter.fluid_ounces_to_liters(sample_fluid_ounces)}')
    print(f'{sample_liters} liters to fluid ounces: {converter.liters_to_fluid_ounces(sample_liters)}')