from dataclasses import dataclass
import math
@dataclass(frozen=True)
class Length:
    value: float
    unit: str
    def __post_init__(self):
        if self.unit not in ["mm", "cm", "m", "km"]:
            raise ValueError("Unsupported unit")
    @staticmethod
    def from_unit(value, target_unit) -> 'Length':
        return Length(
            value * LENGTH_UNITS[target_unit], 
            target_unit
        )
LENGTH_UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0
}
def to_base(length: Length) -> float:
    return length.value * LENGTH_UNITS[length.unit]
def add_length(l1: Length, l2: Length) -> Length:
    base_l1 = to_base(l1)
    base_l2 = to_base(l2)
    total_value = base_l1 + base_l2
    return Length(total_value / LENGTH_UNITS[l1.unit], l1.unit)
def subtract_length(l1: Length, l2: Length) -> Length:
    base_l1 = to_base(l1)
    base_l2 = to_base(l2)
    diff_value = base_l1 - base_l2
    return Length(diff_value / LENGTH_UNITS[l1.unit], l1.unit)
if __name__ == '__main__':
    a = Length(50, "cm")
    b = Length(3.5, "m")
    result_add = add_length(a, b)
    result_sub = subtract_length(b, a)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")