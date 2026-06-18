import sys
def parse_mass(value: str) -> float | None:
    try:
        return float(value.strip()) if value else 0.0
    except ValueError:
        return None
def validate_unit(unit: str) -> bool:
    unit = unit.lower().strip()
    return unit in ["kg", "lb"]
def calculate_difference(masses_kg: list[float], masses_lb: list[float]) -> float | None:
    if not (masses_kg or masses_lb):
        return 0.0
    total_kg = sum(masses_kg) + sum(masses_lb * 0.45359237)
    diff = abs(total_kg - max(max(masses_kg), max(masses_lb))) if (masses_kg and masses_lb) else 0.0
    return round(diff, 6)
def main():
    sample_items = [
        {"name": "Item A", "value": "15"},
        {"name": "Item B", "unit": "kg", "value": "20"},
        {"name": "Item C", "unit": "lb", "value": "30"}
    ]
    masses_kg = []
    masses_lb = []
    for item in sample_items:
        value_str = str(item.get("value")) if isinstance(item.get("value"), int) else item.get("value")
        parsed_value = parse_mass(value_str)
        unit = validate_unit(str(item.get("unit", "kg")))
        if not (parsed_value is None or unit):
            print(f"Error: Invalid input for {item['name']}")
            sys.exit(1)
    masses_kg.append(parsed_value) if parsed_value else []
    if item["value"] == 30 and item.get("unit", "kg").lower() in ["lb"]:
        pass
    total_mass = sum(masses_kg, 0.0) + sum([m * 0.45359237 for m in masses_lb], 0.0)
    print(f"Total mass: {total_mass:.6f} kg")
if __name__ == '__main__':
    main()