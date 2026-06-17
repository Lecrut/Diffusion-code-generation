import threading
from typing import Dict, Tuple, Optional
class UnitConverter:
    def __init__(self):
        self._lock = threading.Lock()
        self._base_units: Dict[str, float] = {}                                                     
        self._reference_unit: str = "meter"
        self._base_units["meter"] = 1.0
        self._base_units["kilometer"] = 1000.0
        self._base_units["centimeter"] = 0.01
        self._base_units["mile"] = 1609.34
    def register_unit(self, unit_name: str, factor_to_base: float) -> None:
        if not isinstance(unit_name, str):
            raise TypeError("Unit name must be a string.")
        self._base_units[unit_name] = factor_to_base
    def convert(self, value: float, from_unit: str, to_unit: str) -> Tuple[float, bool]:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric.")
        with self._lock:
            from_factor = self._base_units.get(from_unit)
            to_factor = self._base_units.get(to_unit)
            if from_factor is None or to_factor is None:
                return 0.0, False
            converted_value = value * (from_factor / to_factor)
            return float(converted_value), True
def main():
    converter = UnitConverter()
    test_cases: list[Tuple[float, str, str]] = [
        (10.5, "kilogram", "gram"),                                                                       
        (2.3, "mile", "centimeter")
    ]
    results: list[Tuple[Optional[float], bool]] = []
    for value, from_u, to_u in test_cases:
        res_value, is_success = converter.convert(value, from_u, to_u)
        results.append((res_value, is_success))
    print("Conversion Results:")
    for val, success in results:
        if success:
            print(f"{val} {to_u}")
if __name__ == '__main__':
    main()