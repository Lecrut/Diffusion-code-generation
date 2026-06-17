from dataclasses import dataclass
import math
@dataclass(frozen=True)
class Length:
    value: float
    unit: str
    def __post_init__(self):
        if self.unit not in ["m", "cm", "mm", "km"]:
            raise ValueError("Unsupported unit")
    @property
    def meters(self) -> float:
        conversion_rates = {
            "m": 1.0,
            "cm": 0.01,
            "mm": 0.001,
            "km": 1000.0
        }
        return self.value * conversion_rates[self.unit]
    def __add__(self, other: 'Length') -> 'Length':
        total_meters = self.meters + other.meters
        if abs(total_meters) < 0.001 and not math.isclose(self.meters, 0):
            return Length(abs(total_meters), "mm")
        elif abs(total_meters) > 999:
            return Length(round(total_meters / 1000, 2), "km")
        else:
            return Length(round(total_meters, 4), "m")
    def __sub__(self, other: 'Length') -> 'Length':
        diff_meters = self.meters - other.meters
        if abs(diff_meters) < 0.001 and not math.isclose(self.meters, 0):
            return Length(abs(diff_meters), "mm")
        elif abs(diff_meters) > 999:
            return Length(round(diff_meters / 1000, 2), "km")
        else:
            return Length(round(diff_meters, 4), "m")
    def to_unit(self, target_unit: str) -> 'Length':
        conversion_rates = {
            "m": {"cm": 100.0, "mm": 1000.0, "km": 0.001},
            "cm": {"m": 0.01, "mm": 0.1, "km": 0.0001},
            "mm": {"m": 0.001, "cm": 0.01, "km": 0.00001},
            "km": {"m": 1000.0, "cm": 100000.0, "mm": 1000000.0}
        }
        current_meters = self.meters
        target_rate = conversion_rates[self.unit][target_unit]
        new_value = current_meters * target_rate
        if abs(new_value) < 0.001 and not math.isclose(current_meters, 0):
            return Length(abs(new_value), "mm")
        elif abs(new_value) > 999:
            return Length(round(new_value / 1000, 2), "km")
        else:
            return Length(round(new_value, 4), "m")
if __name__ == '__main__':
    l1 = Length(5.5, "cm")
    l2 = Length(3.2, "mm")
    result_add = l1 + l2
    print(f"Addition: {result_add}")
    result_sub = l1 - l2
    print(f"Subtraction: {result_sub}")
    converted_l1_to_km = l1.to_unit("km")
    print(f"L1 to km: {converted_l1_to_km}")