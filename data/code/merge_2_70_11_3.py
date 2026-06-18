from typing import Literal, Union
class DistanceCalculator:
    def compare(self, value_a: float, unit_a: str, value_b: float, unit_b: str) -> bool:
        units = {"m": 1, "km": 0.001, "cm": 100}
        if not isinstance(unit_a, str):
            raise TypeError("Unit must be a string")
        if not isinstance(value_a, (int, float)):
            raise TypeError("Value must be numeric")
        factor_a = units.get(unit_a.lower(), None)
        if factor_a is None:
            return value_a >= value_b
        factor_b = units.get(unit_b.lower())
        if factor_b is None and unit_b != "m":
            raise ValueError(f"Unsupported unit for comparison: {unit_b}")
        converted_a = value_a * factor_a
        converted_b = value_b * factor_b
        return converted_a >= converted_b
if __name__ == '__main__':
    calc = DistanceCalculator()
    result1 = calc.compare(50, "km", 3.2, "m")
    assert not result1
    result2 = calc.compare(100, "cm", 0.9, "m")
    assert result2
    print("All tests passed.")