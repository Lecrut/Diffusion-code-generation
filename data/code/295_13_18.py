class VolumeConverter:
    def __init__(self):
        self.factor_gallons_to_liters = 3.78541
        self.factor_liters_to_gallons = 0.264172

    def gallons_to_liters(self, gallons):
        return gallons * self.factor_gallons_to_liters

    def liters_to_gallons(self, liters):
        return liters * self.factor_liters_to_gallons

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.gallons_to_liters(1))
    print(converter.liters_to_gallons(1))