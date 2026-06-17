import math
from typing import Dict, Tuple, Optional, List
from dataclasses import dataclass
@dataclass(frozen=True)
class Unit:
    name: str
    base_value: float = 1.0
@dataclass(frozen=True)
class Quantity:
    value: float
    unit: Unit
    def to_base(self, target_unit: "Unit") -> Tuple[float, Unit]:
        if self.unit == target_unit:
            return (self.value, target_unit)
        ratio = self.unit.base_value / target_unit.base_value
        converted_value = self.value * ratio
        return (converted_value, target_unit)
class UnitConverter:
    _cache: Dict[Tuple[str, str], float] = {}
    def __init__(self):
        self._rates: Dict[Unit, float] = {
            Unit("meter", 1.0),
            Unit("kilometer", 1e3 * 1.0),
            Unit("centimeter", 1e-2 * 1.0),
            Unit("millimeter", 1e-3 * 1.0),
        }
    def _get_rate(self, from_unit: Unit, to_unit: Unit) -> float:
        key = (from_unit.name.lower(), to_unit.name.lower())
        if key in self._cache:
            return self._cache[key]
        rate = from_unit.base_value / to_unit.base_value
        self._cache[key] = rate
        return rate
    def convert(self, quantity: Quantity, target_unit_name: str) -> Quantity:
        if not isinstance(quantity.value, (int, float)):
            raise TypeError("Quantity value must be numeric")
        from_unit = quantity.unit
        to_unit = Unit(target_unit_name.lower(), 1.0)
        rate = self._get_rate(from_unit, to_unit)
        converted_value = quantity.value * rate
        return Quantity(converted_value, to_unit)
def perform_mixed_arithmetic(quantities: List[Quantity], target_units: Dict[str, Unit]) -> Tuple[float, str]:
    converted_list = []
    for q in quantities:
        found_target = False
        for name, u in target_units.items():
            conv_q = converter.convert(q, name)
            if isinstance(conv_q.value, (int, float)):
                converted_list.append(conv_q.value)
                found_target = True
        if not found_target:
             conv_q = converter.convert(q, "meter") 
             converted_list.append(conv_q.value)
    return sum(converted_list), "meter"
if __name__ == '__main__':
    converter = UnitConverter()
    sample_quantities: List[Quantity] = [
        Quantity(10, Unit("kilometer")),
        Quantity(500, Unit("meter")),
        Quantity(-200, Unit("centimeter"))                      
    ]
    target_unit_name = "meters"
    result_quantity: Optional[Quantity] = converter.convert(sample_quantities[0], target_unit_name)
    final_sum_value, _ = perform_mixed_arithmetic(sample_quantities, {"meter": Unit("meter")})
    print(f"Converted {sample_quantities[0]} to meters: {result_quantity.value} m")
    print(f"Mixed arithmetic sum result: {final_sum_value}")