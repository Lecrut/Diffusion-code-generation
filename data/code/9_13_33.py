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
    
    sample_volume_liters = 5.0
    sample_volume_milliliters = 2500.0
    sample_volume_cubic_meters = 0.01
    sample_volume_gallons = 1.32

    print(f"{sample_volume_liters} liters to milliliters: {converter.liters_to_milliliters(sample_volume_liters)} mL")
    print(f"{sample_volume_milliliters} milliliters to liters: {converter.milliliters_to_liters(sample_volume_milliliters)} L")
    print(f"{sample_volume_cubic_meters} m³ to liters: {converter.cubic_meters_to_liters(sample_volume_cubic_meters)} L")
    print(f"{sample_volume_liters} liters to cubic meters: {converter.liters_to_cubic_meters(sample_volume_liters)} m³")
    print(f"{sample_volume_liters} liters to gallons: {converter.liters_to_gallons(sample_volume_liters)} gal")
    print(f"{sample_volume_gallons} gallons to liters: {converter.gallons_to_liters(sample_volume_gallons)} L")