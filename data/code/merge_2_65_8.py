import math
from typing import Dict, Tuple, Optional, List
class UnitConverter:
    def __init__(self) -> None:
        self._cache: Dict[Tuple[str, str], float] = {}
        self.base_rates: Dict[str, float] = {
            "meter": 1.0,
            "kilometer": 1000.0,
            "centimeter": 0.01,
            "mile": 1609.344,
            "foot": 0.3048,
        }
    def _get_rate(self: 'UnitConverter', unit_a: str, unit_b: str) -> float:
        if (unit_a, unit_b) in self._cache:
            return self._cache[(unit_a, unit_b)]
        rate_to_base = self.base_rates.get(unit_a) or 1.0
        rate_from_base = self.base_rates.get(unit_b) or 1.0
        if rate_to_base is None or rate_from_base is None:
            raise ValueError(f"Unsupported units: {unit_a} and {unit_b}")
        conversion_rate = rate_to_base / rate_from_base
        self._cache[(unit_a, unit_b)] = conversion_rate
        return conversion_rate
    def convert(self: 'UnitConverter', value: float, from_unit: str, to_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        rate = self._get_rate(from_unit, to_unit)
        return round(value * rate, 6)
    def get_supported_units(self: 'UnitConverter') -> List[str]:
        return list(self.base_rates.keys())
if __name__ == '__main__':
    converter = UnitConverter()
    sample_tests: List[Tuple[float, str, str]] = [
        (1.0, "meter", "kilometer"),
        (5280.0, "foot", "mile"),
        (3600.0, "second", "hour"),                                                                                                                                                                                                
    ]
    corrected_samples = [
        (1.0, "meter", "kilometer"),
        (5280.0 * 3.28084, "foot", "mile"), 
        (1609.344, "mile", "meter")
    ]
    for val, start_u, end_u in corrected_samples:
        result = converter.convert(val, start_u, end_u)
        print(f"{val} {start_u} -> {result:.2f} {end_u}")