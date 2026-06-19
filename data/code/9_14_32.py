class VolumeConverter:
    def __init__(self):
        self.liter_to_milliliters = 1000
        self.liter_to_gallons = 0.264172
        self.gallon_to_quarts = 4
        self.quart_to_pints = 2
        self.pint_to_cups = 2
        self.cup_to_fluid_ounces = 8

    def liters_to_milliliters(self, liters):
        return liters * self.liter_to_milliliters

    def liters_to_gallons(self, liters):
        return liters * self.liter_to_gallons

    def gallons_to_quarts(self, gallons):
        return gallons * self.gallon_to_quarts

    def quarts_to_pints(self, quarts):
        return quarts * self.quart_to_pints

    def pints_to_cups(self, pints):
        return pints * self.pint_to_cups

    def cups_to_fluid_ounces(self, cups):
        return cups * self.cup_to_fluid_ounces

if __name__ == '__main__':
    converter = VolumeConverter()
    
    sample_liters = 2.5
    print(f"{sample_liters} liters to milliliters: {converter.liters_to_milliliters(sample_liters)}")
    print(f"{sample_liters} liters to gallons: {converter.liters_to_gallons(sample_liters):.4f}")
    
    sample_gallons = 1
    print(f"{sample_gallons} gallons to quarts: {converter.gallons_to_quarts(sample_gallons)}")
    
    sample_quarts = 2
    print(f"{sample_quarts} quarts to pints: {converter.quarts_to_pints(sample_quarts)}")
    
    sample_pints = 4
    print(f"{sample_pints} pints to cups: {converter.pints_to_cups(sample_pints)}")
    
    sample_cups = 8
    print(f"{sample_cups} cups to fluid ounces: {converter.cups_to_fluid_ounces(sample_cups)}")