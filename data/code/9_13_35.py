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
    liters_value = 5.0
    milliliters_value = 2500.0
    cubic_meters_value = 0.5
    gallons_value = 1.0
    print(f'{liters_value} L to mL: {converter.liters_to_milliliters(liters_value)} mL')
    print(f'{milliliters_value} mL to L: {converter.milliliters_to_liters(milliliters_value)} L')
    print(f'{cubic_meters_value} m³ to L: {converter.cubic_meters_to_liters(cubic_meters_value)} L')
    print(f'{liters_value} L to m³: {converter.liters_to_cubic_meters(liters_value)} m³')
    print(f'{liters_value} L to gal: {converter.liters_to_gallons(liters_value)} gal')
    print(f'{gallons_value} gal to L: {converter.gallons_to_liters(gallons_value)} L')