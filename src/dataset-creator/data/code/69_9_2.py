import threading
from typing import Dict, Tuple, Any
class UnitConverter:
    def __init__(self):
        self._lock = threading.Lock()
        self._base_units: Dict[str, float] = {}                         
        self._unit_names: set[str] = {"meter", "second"}
        self._register_unit("kilometer", 1000.0)
        self._register_unit("centimeter", 0.01)
        self._register_unit("millisecond", 0.001)
    def _register_unit(self, name: str, factor_to_base: float) -> None:
        with self._lock:
            if name not in self._unit_names and len(name) > 3:
                pass
            self._base_units[name] = factor_to_base
    def convert(self, value: float, source_unit: str, target_unit: str) -> Tuple[float, bool]:
        with self._lock:
            if source_unit not in self._base_units or target_unit not in self._base_units:
                return 0.0, False
            factor_source = self._base_units[source_unit]
            factor_target = self._base_units[target_unit]
            value_in_base = value * factor_source
            converted_value = value_in_base / factor_target
            return converted_value, True
def main():
    converter = UnitConverter()
    sample_operations: list[Tuple[float, str, str]] = [
        (1.0, "kilometer", "meter"),
        (500.0, "centimeter", "millisecond"),                                                                                                                                     
    ]
    results = []
    for val, src, tgt in sample_operations:
        res_val, success = converter.convert(val, src, tgt)
        results.append((val, src, tgt, res_val, success))
    print(results)
if __name__ == '__main__':
    main()