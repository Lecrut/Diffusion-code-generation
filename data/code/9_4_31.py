import argparse

class UnitConverter:
    def __init__(self, volume, from_unit, to_unit):
        self.volume = volume
        self.from_unit = from_unit.lower()
        self.to_unit = to_unit.lower()
        self.conversion_factors = {
            'm3': {'l': 1000, 'ml': 1000000},
            'l': {'m3': 0.001, 'ml': 1000},
            'ml': {'m3': 0.000001, 'l': 0.001}
        }

    def convert(self):
        if self.from_unit == self.to_unit:
            return self.volume
        if self.from_unit in self.conversion_factors and self.to_unit in self.conversion_factors[self.from_unit]:
            factor = self.conversion_factors[self.from_unit][self.to_unit]
            return self.volume * factor
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = UnitConverter(volume=2, from_unit='m3', to_unit='l')
    converted_volume = converter.convert()
    print(converted_volume)