from typing import Union
class VolumeConverter:
    def __init__(self):
        self.liters = 1.0
        self.milliliters = 1000.0
        self.gallons = 264.172052358148
        self.quarts = 1.0566904799961
        self.pints = 0.528440239998
    def convert_from(self, value: Union[float, int], from_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        units = {
            'liters': self.liters,
            'milliliters': self.milliliters,
            'gallons': self.gallons,
            'quarts': self.quarts,
            'pints': self.pints,
        }
        if from_unit not in units:
            raise ValueError(f"Unsupported unit: {from_unit}. Valid units are liters, milliliters, gallons, quarts, pints.")
        base_value = value / units[from_unit]
        return base_value * 1.0
class VolumeConverter2(VolumeConverter):
    def convert_to(self, value: Union[float, int], to_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        units = {
            'liters': self.liters,
            'milliliters': self.milliliters,
            'gallons': self.gallons,
            'quarts': self.quarts,
            'pints': self.pints,
        }
        if to_unit not in units:
            raise ValueError(f"Unsupported unit: {to_unit}. Valid units are liters, milliliters, gallons, quarts, pints.")
        base_value = value / 1.0
        return base_value * (units[to_unit] / self.liters)
if __name__ == '__main__':
    converter = VolumeConverter2()
    print(converter.convert_from(5, 'liters'))
    print(converter.convert_to(10, 'milliliters'))