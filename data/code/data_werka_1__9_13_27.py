from typing import Union

class VolumeConverter:
    def __init__(self):
        self.liter_to_gallon = 0.264172
        self.gallon_to_liter = 3.78541

    def liters_to_milliliters(self, liters: float) -> float:
        return liters * 1000

    def milliliters_to_liters(self, milliliters: float) -> float:
        return milliliters / 1000

    def liters_to_gallons(self, liters: float) -> float:
        return liters * self.liter_to_gallon

    def gallons_to_liters(self, gallons: float) -> float:
        return gallons * self.gallon_to_liter

    def cubic_meters_to_liters(self, cubic_meters: float) -> float:
        return cubic_meters * 1000

    def liters_to_cubic_meters(self, liters: float) -> float:
        return liters / 1000

if __name__ == '__main__':
    converter = VolumeConverter()
    
    sample_liters = 2.5
    sample_gallons = 1.0
    sample_milliliters = 500.0
    sample_cubic_meters = 0.5

    print(f"{sample_liters} L to mL: {converter.liters_to_milliliters(sample_liters)} mL")
    print(f"{sample_milliliters} mL to L: {converter.milliliters_to_liters(sample_milliliters)} L")
    print(f"{sample_liters} L to gal: {converter.liters_to_gallons(sample_liters)} gal")
    print(f"{sample_gallons} gal to L: {converter.gallons_to_liters(sample_gallons)} L")
    print(f"{sample_cubic_meters} m³ to L: {converter.cubic_meters_to_liters(sample_cubic_meters)} L")
    print(f"{sample_liters} L to m³: {converter.liters_to_cubic_meters(sample_liters)} m³")