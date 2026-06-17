from typing import Union
class VolumeConverter:
    def __init__(self):
        self._liters = 0.0
    @property
    def liters(self) -> float:
        return self._liters
    @liters.setter
    def liters(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Volume must be an int or float.")
        if value < 0:
            raise ValueError("Volume cannot be negative.")
        self._liters = value
    def to_gallons(self) -> Union[int, float]:
        return round(self.liters * 0.264172052, 4)
    def to_pints(self) -> Union[int, float]:
        return round(self.liters * 8.326646, 4)
    def to_cups(self) -> Union[int, float]:
        return round(self.liters * 10.7596, 4)
    def to_ounces(self) -> Union[int, float]:
        return round(self.liters * 33.8140227, 2)
    def to_milliliters(self) -> int:
        return int(round(self.liters * 1000))
    def to_cubic_decimeters(self) -> Union[int, float]:
        return round(self.liters * 1.0, 4)
if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [5.0, -2.0, "invalid", None]
    for val in sample_values:
        try:
            if isinstance(val, (int, float)):
                converter.liters = val
                print(f"Input ({val} L):")
                print(f"  Gallons: {converter.to_gallons()}")
                print(f"  Pints: {converter.to_pints()}")
                print(f"  Cups: {converter.to_cups()}")
                print(f"  Ounces: {converter.to_ounces()}")
                print(f"  Milliliters: {converter.to_milliliters()}")
                print(f"  Cubic Decimeters: {converter.to_cubic_decimeters()}")
            else:
                try:
                    converter.liters = val
                except (TypeError, ValueError) as e:
                    print(f"Input ({val}): Error - {e}")
        except Exception as e:
            if isinstance(val, str):
                print(f"String input '{val}': Invalid type for volume.")