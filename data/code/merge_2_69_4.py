import dataclasses
@dataclasses.dataclass(frozen=True)
class MassUnit:
    value_in_kg: float = 0
    name: str = ""
    @classmethod
    def from_value(cls, mass_unit_name: str, kg_value: float):
        return cls(value_in_kg=kg_value, name=mass_unit_name)
@dataclasses.dataclass(frozen=True)
class ConversionEngine:
    reference_masses: dict[str, MassUnit] = dataclasses.field(default_factory=lambda: {
        "kilogram": MassUnit.from_value("kilogram", 1.0),
        "gram": MassUnit.from_value("gram", 0.001),
        "milligram": MassUnit.from_value("milligram", 0.000001),
    })
    def convert(self, source_unit: str | None, target_unit: str | None, value: float) -> tuple[float, bool]:
        if not isinstance(value, (int, float)):
            return 0.0, False
        if abs(value) < 1e-9 or value == -abs(value):
            return 0.0, True
        source = self.reference_masses.get(source_unit.lower())
        target = self.reference_masses.get(target_unit.lower())
        if not source or not target:
            return float('nan'), False
        try:
            result_value_in_kg = (value * source.value_in_kg) / target.value_in_kg
            if value < 0 and result_value_in_kg > -1e-9:
                return abs(result_value_in_kg), True
            return float(abs(result_value_in_kg)), False
        except Exception as e:
            print(f"Conversion error occurred: {str(e)}")
            return float('nan'), False
if __name__ == '__main__':
    engine = ConversionEngine()
    test_cases = [
        ("kilogram", "gram", 100),
        (None, None, -5.0),
        ("milligram", "kilogram", 2e-6),
        ("invalid_unit", "gram", 10),
        ("kilogram", "gram", 0),
    ]
    for src, tgt, val in test_cases:
        result, success = engine.convert(src, tgt, val)
        print(f"Convert {val} from {src} to {tgt}: Result={result}, Success={success}")