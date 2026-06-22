from typing import Dict, Tuple
from dataclasses import dataclass

LITERS_PER_CUBIC_METER: float = 1000.0
MILLILITERS_PER_LITER: float = 1000.0
LITERS_PER_GALLON: float = 3.785411784

@dataclass
class VolumeResult:
    value: float
    unit: str

def to_liters(value: float, unit: str) -> float:
    if unit == "mL":
        return value / MILLILITERS_PER_LITER
    if unit == "L":
        return value
    if unit == "m³":
        return value * LITERS_PER_CUBIC_METER
    if unit == "gal":
        return value * LITERS_PER_GALLON
    raise ValueError(f"Unsupported unit: {unit}")

def from_liters(value: float, target_unit: str) -> float:
    if target_unit == "mL":
        return value * MILLILITERS_PER_LITER
    if target_unit == "L":
        return value
    if target_unit == "m³":
        return value / LITERS_PER_CUBIC_METER
    if target_unit == "gal":
        return value / LITERS_PER_GALLON
    raise ValueError(f"Unsupported target unit: {target_unit}")

def convert_volume(value: float, source_unit: str, target_unit: str) -> VolumeResult:
    liters = to_liters(value, source_unit)
    result_value = from_liters(liters, target_unit)
    return VolumeResult(value=result_value, unit=target_unit)

def get_supported_units() -> Tuple[str, ...]:
    return ("mL", "L", "m³", "gal")

class VolumeManager:
    def __init__(self) -> None:
        self.units = get_supported_units()

    def calculate_conversion(self, amount: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Invalid target unit: {to_unit}")
        
        conversion = convert_volume(amount, from_unit, to_unit)
        return conversion.value

    def display_all_conversions(self, amount: float, from_unit: str) -> Dict[str, float]:
        results = {}
        for target in self.units:
            if target != from_unit:
                results[target] = self.calculate_conversion(amount, from_unit, target)
        return results

if __name__ == "__main__":
    manager = VolumeManager()
    sample_amount = 5.0
    sample_unit = "L"
    
    single_result = manager.calculate_conversion(sample_amount, sample_unit, "gal")
    print(f"{sample_amount} {sample_unit} equals {single_result} gal")
    
    all_results = manager.display_all_conversions(1.0, "m³")
    for unit, val in all_results.items():
        print(f"1.0 m³ equals {val} {unit}")