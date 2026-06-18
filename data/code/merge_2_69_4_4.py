import dataclasses
@dataclasses.dataclass(frozen=True)
class MassConverter:
    source_unit: str = "kg"
    target_unit: str = "lb"
    value: float = 0.0
    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    def convert(self):
        if self.value <= 0 or not (self.source_unit in ["g", "kg"] and self.target_unit in ["lb", "oz", "tonne"]):
            raise ValueError("Invalid unit combination or non-positive value.")
        conversion_factors = {
            ("kg", "lb"): 2.20462,
            ("kg", "oz"): 35.274,
            ("kg", "tonne"): 1e-3,
            ("g", "lb"): 0.00220462,
            ("g", "oz"): 0.035274,
            ("g", "tonne"): 1e-6,
        }
        factor = conversion_factors.get((self.source_unit, self.target_unit))
        if not factor:
            raise ValueError(f"Unsupported unit pair: {self.source_unit} to {self.target_unit}")
        return round(self.value * factor, 4)
if __name__ == '__main__':
    converter = MassConverter(source_unit="kg", target_unit="lb", value=10.5)
    result = converter.convert()
    print(result)