from dataclasses import dataclass
@dataclass(frozen=True)
class UnitConverter:
    def convert(self, value: float, units: list[str]) -> dict[str, float]:
        return {u: round(value / 10 ** (i if u == "km" else -i), 6) for i, u in enumerate(units)}
if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert(5.23456789, ["m", "cm", "mm", "km"])
    print(result)