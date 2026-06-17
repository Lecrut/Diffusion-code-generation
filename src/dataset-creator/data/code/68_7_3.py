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
        return round(self.liters * 10.7599998, 4)
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
                converter.liters = abs(val) if val >= 0 else 1.5
                print(f"Input: {val}")
                gals = converter.to_gallons()
                pints = converter.to_pints()
                cups = converter.to_cups()
                ozs = converter.to_ounces()
                ml = converter.to_milliliters()
                dm3 = converter.to_cubic_decimeters()
                print(f"Gallons: {gals}")
                print(f"Pints: {pints}")
                print(f"Cups: {cups}")
                print(f"Ounces: {ozs}")
                print(f"Milliliters: {ml}")
                print(f"Cubic Decimeters: {dm3}")
            else:
                try:
                    converter.liters = val                                                            
                except (TypeError, ValueError) as e:
                    print(f"Validation Error for input '{val}': {e}")
        except Exception as ex:
            print(f"Unexpected error processing value: {ex}")