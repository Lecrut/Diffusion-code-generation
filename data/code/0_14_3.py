CONVERSION_FACTORS = {
    "meters": 1.0,
    "kilometers": 1000.0,
    "centimeters": 0.01,
    "millimeters": 0.001,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.344
}

VALID_UNITS = frozenset(CONVERSION_FACTORS.keys())

def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in VALID_UNITS:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in VALID_UNITS:
        raise ValueError(f"Unknown target unit: {to_unit}")
    
    base_value = value * CONVERSION_FACTORS[from_unit]
    result = base_value / CONVERSION_FACTORS[to_unit]
    return result

if __name__ == '__main__':
    print(convert(1, "meters", "kilometers"))
    print(convert(1, "miles", "kilometers"))
    print(convert(1, "inches", "centimeters"))
    print(convert(1, "feet", "meters"))