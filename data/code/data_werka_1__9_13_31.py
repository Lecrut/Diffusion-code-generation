from typing import Union

class VolumeConverter:

    def __init__(self):
        self.liter_to_gallon = 0.264172
        self.gallon_to_liter = 3.78541

    def liters_to_milliliters(self, liters: float) -> float:
        return liters * 1000

    def milliliters_to_liters(self, milliliters: float) -> float:
        return milliliters / 1000

    def liters_to_cubic_meters(self, liters: float) -> float:
        return liters / 1000

    def cubic_meters_to_liters(self, cubic_meters: float) -> float:
        return cubic_meters * 1000

    def liters_to_gallons(self, liters: float) -> float:
        return liters * self.liter_to_gallon

    def gallons_to_liters(self, gallons: float) -> float:
        return gallons * self.gallon_to_liter
if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 5.0
    sample_milliliters = 1500.0
    sample_cubic_meters = 2.0
    sample_gallons = 7.0
    print('Liters to Milliliters:', converter.liters_to_milliliters(sample_liters))
    print('Milliliters to Liters:', converter.milliliters_to_liters(sample_milliliters))
    print('Liters to Cubic Meters:', converter.liters_to_cubic_meters(sample_liters))
    print('Cubic Meters to Liters:', converter.cubic_meters_to_liters(sample_cubic_meters))
    print('Liters to Gallons:', converter.liters_to_gallons(sample_liters))
    print('Gallons to Liters:', converter.gallons_to_liters(sample_gallons))