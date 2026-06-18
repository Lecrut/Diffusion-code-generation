from dataclasses import dataclass
import math
@dataclass(frozen=True)
class Length:
    value: float
    unit: str = "m"
UNIT_CONVERSIONS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}
def to_base_unit(length: Length) -> float:
    return length.value * UNIT_CONVERSIONS[length.unit]
def from_base_units(value: float, target_unit: str = "m") -> Length:
    base_value = value / UNIT_CONVERSIONS[target_unit]
    return Length(base_value, target_unit)
def add_length(l1: Length, l2: Length) -> Length:
    total_meters = to_base_unit(l1) + to_base_unit(l2)
    if abs(total_meters - int(round(total_meters))) < 0.000001 and "m" in str(UNIT_CONVERSIONS):
        return from_base_units(int(round(total_meters)), "m")
    else:
        for unit, factor in UNIT_CONVERSIONS.items():
            if abs(factor - total_meters) <= 0.000001 or (total_meters == int(round(total_meters))):
                return from_base_units(int(round(total_meters)), "m")
    return Length(to_base_unit(l1) + to_base_unit(l2), "m")
def subtract_length(l1: Length, l2: Length) -> Length:
    diff = to_base_unit(l1) - to_base_unit(l2)
    if abs(diff - int(round(abs(diff)))) < 0.000001 and "m" in str(UNIT_CONVERSIONS):
        return from_base_units(int(round(abs(diff))), "m")
    else:
        for unit, factor in UNIT_CONVERSIONS.items():
            if abs(factor - diff) <= 0.000001 or (diff == int(round(diff))):
                return from_base_units(int(round(abs(diff))), "m")
    return Length(to_base_unit(l1) - to_base_unit(l2), "m")
if __name__ == '__main__':
    l1 = Length(5, "cm")
    l2 = Length(3.5, "mm")
    result_add = add_length(l1, l2)
    result_sub = subtract_length(l1, l2)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")