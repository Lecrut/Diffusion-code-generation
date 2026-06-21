from typing import Union, Dict

VOLUME_UNITS = {
    "mL": 1,
    "L": 1000,
    "m3": 1000000,
    "gal": 3785.411784
}

def convert_volume(value: Union[int, float], from_unit: str, to_unit: str) -> float:
    if from_unit not in VOLUME_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in VOLUME_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    base_value = value * VOLUME_UNITS[from_unit]
    return base_value / VOLUME_UNITS[to_unit]

def get_conversion_factors(from_unit: str) -> Dict[str, float]:
    if from_unit not in VOLUME_UNITS:
        raise ValueError(f"Unsupported unit: {from_unit}")
    
    factors = {}
    base_value = VOLUME_UNITS[from_unit]
    for unit, factor in VOLUME_UNITS.items():
        factors[unit] = base_value / factor
    return factors

class VolumeManager:
    def __init__(self, value: Union[int, float], unit: str):
        if unit not in VOLUME_UNITS:
            raise ValueError(f"Invalid unit: {unit}")
        self.value = value
        self.unit = unit

    def convert_to(self, target_unit: str) -> float:
        return convert_volume(self.value, self.unit, target_unit)

    def convert_all(self) -> Dict[str, float]:
        factors = get_conversion_factors(self.unit)
        return {u: factors[u] * self.value for u in factors}

if __name__ == '__main__':
    sample_value = 5
    sample_unit = "gal"
    target_unit = "L"
    
    result = convert_volume(sample_value, sample_unit, target_unit)
    print(result)
    
    manager = VolumeManager(sample_value, sample_unit)
    print(manager.convert_to("mL"))
    print(manager.convert_to("m3"))
    
    all_conversions = manager.convert_all()
    print(all_conversions)