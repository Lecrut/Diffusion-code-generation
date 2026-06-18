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
        self._liters = float(value)
    def to_gallons(self) -> Union[int, float]:
        return round(self.liters * 0.264172052, 3)
    def to_pints(self) -> Union[int, float]:
        return round(self.liters * 8.45350567, 3)
    def to_cups(self) -> Union[int, float]:
        return round(self.liters * 12.99998695, 3)
    def to_ounces(self) -> Union[int, float]:
        return round(self.liters * 47.03772818, 3)
    def to_milliliters(self) -> int:
        return int(round(self.liters * 1000))
    def to_cubic_decimeters(self) -> Union[int, float]:
        return round(self.liters, 3)
if __name__ == '__main__':
    converter = VolumeConverter()
    samples: list[dict[str, Union[int, float]]] = [
        {"liters": 1.0},
        {"liters": 5.7362984},
        {"liters": -1.0}
    ]
    try:
        for sample in samples:
            converter.liters = sample["liters"]
            print(f"Input (Liters): {sample['liters']}")
            print("  Gallons:", converter.to_gallons())
            print("  Pints:", converter.to_pints())
            print("  Cups:", converter.to_cups())
            print("  Ounces:", converter.to_ounces())
            print("  Milliliters:", converter.to_milliliters())
            print("  Cubic Decimeters:", converter.to_cubic_decimeters())
    except (ValueError, TypeError) as e:
        print(f"Validation Error: {e}")