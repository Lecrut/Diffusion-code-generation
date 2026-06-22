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

    def convert_volume(self, value: float, from_unit: str, to_unit: str) -> Union[float, None]:
        if from_unit == 'L' and to_unit == 'mL':
            return self.liters_to_milliliters(value)
        elif from_unit == 'mL' and to_unit == 'L':
            return self.milliliters_to_liters(value)
        elif from_unit == 'L' and to_unit == 'gal':
            return self.liters_to_gallons(value)
        elif from_unit == 'gal' and to_unit == 'L':
            return self.gallons_to_liters(value)
        elif from_unit == 'm³' and to_unit == 'L':
            return self.cubic_meters_to_liters(value)
        elif from_unit == 'L' and to_unit == 'm³':
            return self.liters_to_cubic_meters(value)
        else:
            raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert_volume(1.0, 'L', 'mL'))
    print(converter.convert_volume(500.0, 'mL', 'L'))
    print(converter.convert_volume(2.0, 'L', 'gal'))
    print(converter.convert_volume(1.0, 'gal', 'L'))
    print(converter.convert_volume(1.0, 'm³', 'L'))
    print(converter.convert_volume(1000.0, 'L', 'm³'))