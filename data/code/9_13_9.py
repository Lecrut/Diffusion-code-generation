from typing import Union
from dataclasses import dataclass

@dataclass(frozen=True)
class Volume:
    liters: float

    def to_milliliters(self) -> float:
        return self.liters * 1000

    def to_cubic_meters(self) -> float:
        return self.liters / 1000

    def to_gallons(self) -> float:
        return self.liters / 3.785411784

def convert_to_liters(value: Union[float, int], unit: str) -> float:
    unit_lower = unit.lower()
    if unit_lower == 'l' or unit_lower == 'liter' or unit_lower == 'liters':
        return float(value)
    elif unit_lower == 'ml' or unit_lower == 'milliliter' or unit_lower == 'milliliters':
        return float(value) / 1000
    elif unit_lower == 'm3' or unit_lower == 'm3' or unit_lower == 'cubic meter' or unit_lower == 'cubic meters':
        return float(value) * 1000
    elif unit_lower == 'gal' or unit_lower == 'gallon' or unit_lower == 'gallons':
        return float(value) * 3.785411784
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def convert_volume(value: Union[float, int], from_unit: str, to_unit: str) -> float:
    liters = convert_to_liters(value, from_unit)
    target_volume = Volume(liters=liters)
    
    to_lower = to_unit.lower()
    if to_lower == 'l' or to_lower == 'liter' or to_lower == 'liters':
        return liters
    elif to_lower == 'ml' or to_lower == 'milliliter' or to_lower == 'milliliters':
        return target_volume.to_milliliters()
    elif to_lower == 'm3' or to_lower == 'm3' or to_lower == 'cubic meter' or to_lower == 'cubic meters':
        return target_volume.to_cubic_meters()
    elif to_lower == 'gal' or to_lower == 'gallon' or to_lower == 'gallons':
        return target_volume.to_gallons()
    else:
        raise ValueError(f"Unsupported target unit: {to_unit}")

if __name__ == '__main__':
    sample_volume_val = 2.5
    sample_from_unit = 'gal'
    sample_to_unit = 'l'
    result_1 = convert_volume(sample_volume_val, sample_from_unit, sample_to_unit)
    print(result_1)
    
    sample_to_unit_2 = 'ml'
    result_2 = convert_volume(sample_volume_val, sample_from_unit, sample_to_unit_2)
    print(result_2)
    
    sample_to_unit_3 = 'm3'
    result_3 = convert_volume(sample_volume_val, sample_from_unit, sample_to_unit_3)
    print(result_3)
    
    vol_instance = Volume(liters=100.0)
    print(vol_instance.to_milliliters())
    print(vol_instance.to_cubic_meters())
    print(vol_instance.to_gallons())