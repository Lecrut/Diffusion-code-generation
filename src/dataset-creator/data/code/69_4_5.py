from dataclasses import dataclass
@dataclass(frozen=True)
class MassUnit:
    value: float
    unit_name: str = "kg"
def convert_mass(source_unit: MassUnit, target_unit: str) -> MassUnit:
    conversion_rates = {
        "g": 0.001,
        "mg": 1e-6,
        "t": 1_000_000,
        "kg": 1,
        "lb": 0.45359237,
    }
    if source_unit.value <= 0:
        raise ValueError("Mass value must be positive.")
    rate = conversion_rates.get(target_unit.lower())
    if not rate or target_unit.lower() == source_unit.unit_name.lower():
        return MassUnit(value=source_unit.value)
    converted_value = source_unit.value * (conversion_rates[source_unit.unit_name] / rate)
    return MassUnit(value=converted_value, unit_name=target_unit.upper())
if __name__ == '__main__':
    sample_input = MassUnit(value=100.5, unit_name="kg")
    try:
        result_kg = convert_mass(sample_input, "kg")
        print(f"{sample_input.value} {sample_input.unit_name} -> {result_kg.value} kg")
        result_g = convert_mass(sample_input, "g")
        print(f"{sample_input.value} {sample_input.unit_name} -> {result_g.value} g")
        result_lb = convert_mass(sample_input, "lb")
        print(f"{sample_input.value} {sample_input.unit_name} -> {result_lb.value} lb")
    except ValueError as e:
        print(e)