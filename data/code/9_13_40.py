from typing import Union

class VolumeConverter:

    def __init__(self):
        self.liter_to_gallon = 0.264172
        self.gallon_to_liter = 3.78541

    def liters_to_milliliters(self, liters: float) -> float:
        return liters * 1000

    def milliliters_to_liters(self, milliliters: float) -> float:
        return milliliters / 1000

    def cubic_meters_to_liters(self, cubic_meters: float) -> float:
        return cubic_meters * 1000

    def liters_to_cubic_meters(self, liters: float) -> float:
        return liters / 1000

    def liters_to_gallons(self, liters: float) -> float:
        return liters * self.liter_to_gallon

    def gallons_to_liters(self, gallons: float) -> float:
        return gallons * self.gallon_to_liter
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(1500))
    print(converter.cubic_meters_to_liters(3))
    print(converter.liters_to_cubic_meters(4000))
    print(converter.liters_to_gallons(10))
    print(converter.gallons_to_liters(5))