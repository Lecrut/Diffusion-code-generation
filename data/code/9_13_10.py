from enum import Enum
from typing import Union

class VolumeUnit(Enum):
    MILLILITER = "mL"
    LITER = "L"
    CUBIC_METER = "m3"
    GALLON = "gal"

    def to_liter(self, value: float) -> float:
        if self == VolumeUnit.MILLILITER:
            return value / 1000.0
        if self == VolumeUnit.LITER:
            return value
        if self == VolumeUnit.CUBIC_METER:
            return value * 1000.0
        if self == VolumeUnit.GALLON:
            return value * 3.785411784
        raise ValueError(f"Unsupported unit: {self}")

    def from_liter(self, value: float) -> float:
        if self == VolumeUnit.MILLILITER:
            return value * 1000.0
        if self == VolumeUnit.LITER:
            return value
        if self == VolumeUnit.CUBIC_METER:
            return value / 1000.0
        if self == VolumeUnit.GALLON:
            return value / 3.785411784
        raise ValueError(f"Unsupported unit: {self}")

def convert_volume(value: float, from_unit: VolumeUnit, to_unit: VolumeUnit) -> float:
    if from_unit == to_unit:
        return value
    liter_value = from_unit.to_liter(value)
    return to_unit.from_liter(liter_value)

class VolumeManager:
    def __init__(self, value: float, unit: VolumeUnit):
        self.value = value
        self.unit = unit

    def convert_to(self, target_unit: VolumeUnit) -> float:
        return convert_volume(self.value, self.unit, target_unit)

    def add(self, other: "VolumeManager") -> "VolumeManager":
        total_liters = self.unit.to_liter(self.value) + other.unit.to_liter(other.value)
        return VolumeManager(total_liters, VolumeUnit.LITER)

    def __repr__(self) -> str:
        return f"{self.value} {self.unit.value}"

if __name__ == "__main__":
    initial_volume = 5.0
    input_unit = VolumeUnit.GALLON
    output_unit = VolumeUnit.LITER
    converted_result = convert_volume(initial_volume, input_unit, output_unit)
    print(converted_result)

    manager = VolumeManager(1.0, VolumeUnit.CUBIC_METER)
    gallons_result = manager.convert_to(VolumeUnit.GALLON)
    print(gallons_result)

    v1 = VolumeManager(2.0, VolumeUnit.LITER)
    v2 = VolumeManager(1000.0, VolumeUnit.MILLILITER)
    sum_manager = v1.add(v2)
    print(sum_manager.convert_to(VolumeUnit.MILLILITER))