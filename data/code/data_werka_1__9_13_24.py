from typing import Union

class VolumeConverter:
    def __init__(self):
        self.liter_to_gallon = 0.264172
        self.m3_to_liter = 1000

    def liters_to_milliliters(self, liters: float) -> float:
        return liters * 1000

    def milliliters_to_liters(self, milliliters: float) -> float:
        return milliliters / 1000

    def cubic_meters_to_liters(self, cubic_meters: float) -> float:
        return cubic_meters * self.m3_to_liter

    def liters_to_gallons(self, liters: float) -> float:
        return liters * self.liter_to_gallon

    def gallons_to_liters(self, gallons: float) -> float:
        return gallons / self.liter_to_gallon

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 2.0
    sample_milliliters = 500.0
    sample_cubic_meters = 1.0
    sample_gallons = 1.0

    print(f"{sample_liters} liters to milliliters: {converter.liters_to_milliliters(sample_liters)}")
    print(f"{sample_milliliters} milliliters to liters: {converter.milliliters_to_liters(sample_milliliters)}")
    print(f"{sample_cubic_meters} cubic meters to liters: {converter.cubic_meters_to_liters(sample_cubic_meters)}")
    print(f"{sample_liters} liters to gallons: {converter.liters_to_gallons(sample_liters)}")
    print(f"{sample_gallons} gallons to liters: {converter.gallons_to_liters(sample_gallons)}")