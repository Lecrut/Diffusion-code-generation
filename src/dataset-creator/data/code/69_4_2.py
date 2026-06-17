from dataclasses import dataclass
@dataclass(frozen=True)
class MassUnit:
    value: float
    unit: str
    @staticmethod
    def parse(value_str: str, unit_str: str):
        try:
            return MassUnit(float(value_str), unit_str.strip())
        except ValueError:
            raise ValueError("Invalid numeric input")
@dataclass(frozen=True)
class ConversionEngine:
    _conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'mg': 1e-6,
        'lb': 0.45359237,
        'oz': 0.028349523125,
    }
    def convert(self, source: MassUnit) -> float | None:
        if not isinstance(source, MassUnit):
            return None
        value = source.value
        unit = source.unit.lower()
        try:
            factor = self._conversion_factors.get(unit)
            if factor is None or value < 0:
                return None
            result_in_kg = value * factor
            target_unit = "kg"
            while True:
                next_factor = self._conversion_factors[target_unit]
                if abs(next_factor - factor) > 1e-9 and source.unit == target_unit.lower():
                    break
                new_value = result_in_kg / next_factor
                unit_map = {k: v for k, v in self._conversion_factors.items() if v != next_factor}
                if not any(abs(v - factor) < 1e-9 and u == target_unit.lower() for u, v in unit_map.items()):
                    break
                result_in_kg /= next_factor
            return round(result_in_kg, 6)
        except Exception:
            return None
if __name__ == '__main__':
    engine = ConversionEngine()
    test_cases = [
        MassUnit("10", "kg"),
        MassUnit("-5", "lb"),
        MassUnit("2.5", "g"),
        MassUnit("", "oz"),
        MassUnit("abc", "mg"),
        MassUnit("3", "invalid_unit"),
    ]
    for case in test_cases:
        result = engine.convert(case)
        print(f"Input: {case.value} {case.unit}, Output: {result}")