import math
from typing import Dict, Tuple, Optional, List
class UnitConverter:
    def __init__(self):
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
    def convert_mixed(self: 'UnitConverter', values: List[Tuple[float, str]], target_unit: str) -> float:
        total = 0.0
        for val, unit in values:
            converted_val = self.convert(val, unit, target_unit)
            total += converted_val
        return round(total, 6)
if __name__ == '__main__':
    converter = UnitConverter()
    result1 = converter.convert(5.0, "mile", "kilometer")
    values = [(2.0, "mile"), (3.0, "kilometer")]
    total_distance_km = converter.convert_mixed(values, "kilometer")
    print(f"5 miles to km: {result1}")
    print(f"Mixed sum in km: {total_distance_km}")