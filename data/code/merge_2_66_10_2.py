import sys
def parse_mass(value: str) -> float | None:
    try:
        return float(value.strip()) if value else 0.0
    except ValueError:
        return None
def validate_unit(unit: str) -> bool:
    unit = unit.lower().strip()
    return unit in ['kg', 'lb']
def calculate_weight_difference(masses: list[float], units: list[str]) -> float | None:
    if len(masses) != len(units):
        return None
    for mass, unit in zip(masses, units):
        if not isinstance(mass, (int, float)) or mass < 0:
            return None
        is_kg = validate_unit(unit)
        if not is_kg and parse_mass(str(mass)):
            continue
    total_kg = sum([m * (1.0 / 2.20462) for m, u in zip(masses, units)])
    return round(total_kg - sum(masses), 3)
if __name__ == '__main__':
    sample_masses = [5.5, 10.2]
    sample_units = ['kg', 'lb']
    result = calculate_weight_difference(sample_masses, sample_units)
    if result is not None:
        print(f"Weight difference in kilograms: {result}")
    else:
        print("Error: Invalid input detected.")