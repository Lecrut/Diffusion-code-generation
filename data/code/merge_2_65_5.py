from dataclasses import dataclass
import math
@dataclass(frozen=True)
class Length:
    value: float
    unit: str = "m"
    def __post_init__(self):
        if self.unit not in ["mm", "cm", "dm", "m", "km"]:
            raise ValueError("Unsupported unit")
UNIT_TO_METER = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1.0,
    "km": 1000.0,
}
def to_meters(length: Length) -> float:
    return length.value * UNIT_TO_METER[length.unit]
def from_meters(value: float, target_unit: str) -> Length:
    meters = value / UNIT_TO_METER[target_unit] if target_unit in ["mm", "cm", "dm"] else value
    if target_unit == "m":
        return Length(value / UNIT_TO_METER["m"])
    else:
        factor = 1 / UNIT_TO_METER[target_unit]
        return Length(value * factor)
def add(lengths):
    total_meters = sum(to_meters(l) for l in lengths)
    return Length(total_meters, "m")
def subtract(lengths):
    total_meters = sum(to_meters(l) * -1 for l in lengths[1:]) + to_meters(lengths[0])
    return Length(total_meters, "m")
if __name__ == '__main__':
    a = Length(5, "km")
    b = Length(2.5, "cm")
    c = add([a, b])
    d = subtract([c, Length(100, "mm")])
    print(f"Result: {d}")