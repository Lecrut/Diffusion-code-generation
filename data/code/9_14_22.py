class VolumeConverter:
    def __init__(self):
        self.liter_to_milliliter = 1000
        self.liter_to_gallon = 0.264172
        self.liter_to_quart = 1.05669
        self.liter_to_pint = 2.11338
        self.liter_to_cup = 4.22675
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

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 2.5
    print("Liters to Milliliters:", converter.liters_to_milliliters(sample_liters))
    print("Liters to Gallons:", converter.liters_to_gallons(sample_liters))
    print("Liters to Quarts:", converter.liters_to_quarts(sample_liters))
    print("Liters to Pints:", converter.liters_to_pints(sample_liters))
    print("Liters to Cups:", converter.liters_to_cups(sample_liters))
    print("Liters to Fluid Ounces:", converter.liters_to_fluid_ounces(sample_liters))