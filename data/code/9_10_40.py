class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_LITERS = 3.78541
    QUARTS_TO_LITERS = 0.946353
    PINTS_TO_LITERS = 0.473176
    CUPS_TO_LITERS = 0.236588
    FLUID_OUNCES_TO_LITERS = 0.0295735

    @staticmethod
    def liters_to_milliliters(liters):
        return liters * VolumeConverter.LITERS_TO_MILLILITERS

    @staticmethod
    def milliliters_to_liters(milliliters):
        return milliliters / VolumeConverter.LITERS_TO_MILLILITERS

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * VolumeConverter.GALLONS_TO_LITERS

    @staticmethod
    def liters_to_gallons(liters):
        return liters / VolumeConverter.GALLONS_TO_LITERS

    @staticmethod
    def quarts_to_liters(quarts):
        return quarts * VolumeConverter.QUARTS_TO_LITERS

    @staticmethod
    def liters_to_quarts(liters):
        return liters / VolumeConverter.QUARTS_TO_LITERS

    @staticmethod
    def pints_to_liters(pints):
        return pints * VolumeConverter.PINTS_TO_LITERS

    @staticmethod
    def liters_to_pints(liters):
        return liters / VolumeConverter.PINTS_TO_LITERS

    @staticmethod
    def cups_to_liters(cups):
        return cups * VolumeConverter.CUPS_TO_LITERS

    @staticmethod
    def liters_to_cups(liters):
        return liters / VolumeConverter.CUPS_TO_LITERS

    @staticmethod
    def fluid_ounces_to_liters(fluid_ounces):
        return fluid_ounces * VolumeConverter.FLUID_OUNCES_TO_LITERS

    @staticmethod
    def liters_to_fluid_ounces(liters):
        return liters / VolumeConverter.FLUID_OUNCES_TO_LITERS
if __name__ == '__main__':
    print('1 liter to milliliters:', VolumeConverter.liters_to_milliliters(1))
    print('1000 milliliters to liters:', VolumeConverter.milliliters_to_liters(1000))
    print('1 gallon to liters:', VolumeConverter.gallons_to_liters(1))
    print('3.78541 liters to gallons:', VolumeConverter.liters_to_gallons(3.78541))
    print('1 quart to liters:', VolumeConverter.quarts_to_liters(1))
    print('0.946353 liters to quarts:', VolumeConverter.liters_to_quarts(0.946353))
    print('1 pint to liters:', VolumeConverter.pints_to_liters(1))
    print('0.473176 liters to pints:', VolumeConverter.liters_to_pints(0.473176))
    print('1 cup to liters:', VolumeConverter.cups_to_liters(1))
    print('0.236588 liters to cups:', VolumeConverter.liters_to_cups(0.236588))
    print('1 fluid ounce to liters:', VolumeConverter.fluid_ounces_to_liters(1))
    print('0.0295735 liters to fluid ounces:', VolumeConverter.liters_to_fluid_ounces(0.0295735))