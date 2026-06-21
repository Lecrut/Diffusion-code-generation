from typing import Union
from dataclasses import dataclass

@dataclass
class Volume:
    value: float
    unit: str

    def to_liters(self) -> float:
        if self.unit == "L":
            return self.value
        if self.unit == "mL":
            return self.value / 1000.0
        if self.unit == "m3":
            return self.value * 1000.0
        if self.unit == "gal":
            return self.value * 3.785411784
        raise ValueError("Unsupported unit")

    def to(self, target_unit: str) -> float:
        liters = self.to_liters()
        if target_unit == "L":
            return liters
        if target_unit == "mL":
            return liters * 1000.0
        if target_unit == "m3":
            return liters / 1000.0
        if target_unit == "gal":
            return liters / 3.785411784
        raise ValueError("Unsupported target unit")

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    volume = Volume(value, from_unit)
    return volume.to(to_unit)

if __name__ == '__main__':
    liters_to_gallons = convert_volume(10.0, "L", "gal")
    milliliters_to_liters = convert_volume(500.0, "mL", "L")
    cubic_meters_to_gallons = convert_volume(2.5, "m3", "gal")
    gallons_to_liters = convert_volume(5.0, "gal", "L")
    print(liters_to_gallons)
    print(milliliters_to_liters)
    print(cubic_meters_to_gallons)
    print(gallons_to_liters)