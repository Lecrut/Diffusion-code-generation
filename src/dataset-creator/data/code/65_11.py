from dataclasses import dataclass
@dataclass(frozen=True)
class LengthUnit:
    name: str
    factor: float
UNITS = [LengthUnit("meter", 1), LengthUnit("kilometer", 0.001), LengthUnit("centimeter", 100)]
def convert_length(value_str: str) -> dict[str, int | float]:
    try:
        value = float(value_str.strip())
    except ValueError:
        raise ValueError(f"Invalid input: {value_str}")
    return {unit.name: round(unit.factor * value, 6) for unit in UNITS}
if __name__ == '__main__':
    print(convert_length("150"))