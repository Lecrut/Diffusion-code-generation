import threading
from typing import Union
class UnitConverter:
    def __init__(self):
        self._lock = threading.Lock()
        self._conversion_factors = {
            "meter": 1.0,
            "kilometer": 1000.0,
            "centimeter": 0.01,
            "mile": 1609.34,
            "foot": 0.3048,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> Union[float, None]:
        if not isinstance(value, (int, float)):
            return None
        with self._lock:
            factor_from = self._conversion_factors.get(from_unit.lower())
            factor_to = self._conversion_factors.get(to_unit.lower())
            if factor_from is None or factor_to is None:
                return None
            base_value = value * factor_from
            converted_value = base_value / factor_to
            return round(converted_value, 6)
if __name__ == '__main__':
    converter = UnitConverter()
    samples = [
        ("10", "kilometer", "meter"),
        ("5.2", "mile", "foot"),
        ("100", "centimeter", "meter"),
        (3, "meter", "kilometer")
    ]
    results: list[Union[float, None]] = []
    for val_str, u_from, u_to in samples:
        value = float(val_str)
        result = converter.convert(value, u_from, u_to)
        if result is not None:
            results.append(result)
        print(f"{val_str} {u_from} to {u_to}: {result}")