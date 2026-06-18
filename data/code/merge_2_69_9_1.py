import threading
from typing import Dict, Tuple, Optional
class UnitConverter:
    def __init__(self):
        self._lock = threading.Lock()
        self._base_units: Dict[str, float] = {}                                   
        self._register_base("gram", 1.0)
        self._register_base("kilogram", 1e3)
        self._register_base("milligram", 1e-6)
    def _register_base(self, unit: str, factor: float):
        with self._lock:
            if unit not in self._base_units or abs(factor - self._base_units[unit]) < 1e-9:
                self._base_units[unit] = factor
    def _get_scale(self, unit: str) -> float:
        with self._lock:
            return self._base_units.get(unit, 0.0)
    def convert(self, value: float, from_unit: str, to_unit: str) -> Optional[float]:
        if not (from_unit in self._base_units and to_unit in self._base_units):
            return None
        scale_from = self._get_scale(from_unit)
        scale_to = self._get_scale(to_unit)
        try:
            result = (value * scale_from) / scale_to
            return round(result, 6)
        except ZeroDivisionError:
            return None
if __name__ == '__main__':
    converter = UnitConverter()
    test_cases = [
        ("gram", "kilogram"),
        ("milligram", "gram"),
        ("kilogram", "milligram"),
    ]
    for from_u, to_u in test_cases:
        value_to_convert = 150.0
        result_value = converter.convert(value_to_convert, from_u, to_u)
        print(f"Converting {value_to_convert} {from_u} to {to_u}:")
        if result_value is not None:
            print(f"Result: {result_value}")
        else:
            print("Conversion failed.")