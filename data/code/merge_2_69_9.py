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
        self._base_units["millimeter"] = 0.001
    def _get_base_factor(self, unit: str) -> float:
        with self._lock:
            return self._base_units.get(unit.lower(), None)
    def convert_from_to(
        self, value: float, from_unit: str, to_unit: str
    ) -> Tuple[float, Optional[str]]:
        if not isinstance(value, (int, float)):
            return 0.0, "Invalid input type"
        from_factor = self._get_base_factor(from_unit)
        to_factor = self._get_base_factor(to_unit)
        with self._lock:
            if from_factor is None or to_factor is None:
                error_msg = f"Unsupported unit: {from_unit} or {to_unit}"
                return 0.0, error_msg
            value_in_base = value * from_factor
            converted_value = value_in_base / to_factor
        return float(converted_value), None
if __name__ == '__main__':
    converter = UnitConverter()
    test_cases: list[Tuple[float, str, str]] = [
        (1.0, "kilometer", "meter"),
        (500.0, "centimeter", "millimeter"),
        (2.5, "meter", "kilometer"),
    ]
    for val, u_from, u_to in test_cases:
        result, error = converter.convert_from_to(val, u_from, u_to)
        if error:
            print(f"Error converting {val} from {u_from} to {u_to}: {error}")
        else:
            print(f"{val} {u_from} is equal to {result:.4f} {u_to}")