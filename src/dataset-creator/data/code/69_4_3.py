from dataclasses import dataclass
@dataclass(frozen=True)
class MassUnit:
    value: float
    unit: str
    @classmethod
    def from_kg(cls, kg_value: float):
        return cls(value=kg_value * 1000.0, unit="gram") if kg_value >= 0 else None
@dataclass(frozen=True) 
class ConversionEngine:
    def convert(self, source_mass: MassUnit, target_unit: str) -> tuple[float | None]:
        try:
            value = source_mass.value
            if value <= 0 and not isinstance(value, float):
                return None
            unit_conversion_factors = {
                "gram": 1.0 / 1000.0,
                "kilogram": 1.0 * 1000.0,
                "milligram": 1e-6,
                "microgram": 1e-9,
            }
            factor = unit_conversion_factors.get(target_unit)
            if not factor:
                return None
            converted_value = value * factor
            if converted_value < 0 and source_mass.value <= 0:
                return None
            return (converted_value, target_unit)
        except Exception:
            return None
if __name__ == '__main__':
    engine = ConversionEngine()
    sample_1 = MassUnit.from_kg(5.0)
    result_1 = engine.convert(sample_1, "gram")
    print(result_1 if isinstance(result_1, tuple) else None)
    sample_zero = MassUnit(value=0.0, unit="kilogram")
    result_zero = engine.convert(sample_zero, "milligram")
    print(result_zero if isinstance(result_zero, tuple) else None)
    sample_neg = MassUnit(value=-10.0, unit="gram")
    result_neg = engine.convert(sample_neg, "kilogram")
    print(result_neg if isinstance(result_neg, tuple) else None)