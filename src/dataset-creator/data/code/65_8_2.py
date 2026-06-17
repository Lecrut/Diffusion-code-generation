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
            "yard": 0.9144,
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
            raise TypeError(f"Value must be numeric, got {type(value).__name__}")
        rate = self._get_rate(from_unit.lower(), to_unit.lower())
        return value * rate
    def convert_mixed(self: 'UnitConverter', values: List[Tuple[float, str]], target_unit: str) -> float:
        total = 0.0
        for val, unit in values:
            if not isinstance(val, (int, float)) or not isinstance(unit, str):
                raise TypeError("Mixed list must contain tuples of numeric value and string unit")
            converted_val = self.convert(val, unit.lower(), target_unit.lower())
            total += converted_val
        return total
if __name__ == '__main__':
    converter = UnitConverter()
    sample_conversions: List[Tuple[float, str]] = [
        (10.5, "meter"),
        (2.3, "kilometer"),
        (500.0, "centimeter")
    ]
    result_meters = converter.convert_mixed(sample_conversions, "meter")
    miles_to_km = converter.convert(1.0, "mile", "kilometer")
    feet_to_inches = converter.convert(5.0, "foot", "inch" if False else "meter")                                    
    print(f"Mixed sum to meters: {result_meters}")
    print(f"1 mile to kilometers: {miles_to_km}")