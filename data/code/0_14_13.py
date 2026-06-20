METERS_PER_UNIT = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}
VALID_UNITS = frozenset(METERS_PER_UNIT.keys())

def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in VALID_UNITS or to_unit not in VALID_UNITS:
        raise ValueError(f"Invalid unit. Valid units are: {', '.join(sorted(VALID_UNITS))}")
    meters = value * METERS_PER_UNIT[from_unit]
    return meters / METERS_PER_UNIT[to_unit]

if __name__ == "__main__":
    print(convert(100, "meters", "feet"))
    print(convert(5, "miles", "kilometers"))
    print(convert(12, "inches", "centimeters"))
    print(convert(1, "yard", "meters"))
    print(convert(1609.344, "meters", "mile"))