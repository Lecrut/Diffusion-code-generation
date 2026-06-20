UNIT_CONVERSION_FACTORS = {
    "meters_to_feet": 3.28084,
    "meters_to_inches": 39.3701,
    "meters_to_yards": 1.09361
}

def convert_unit(value: float, factor_key: str) -> float:
    factor = UNIT_CONVERSION_FACTORS.get(factor_key)
    if factor is None:
        raise ValueError(f"Unknown conversion key: {factor_key}")
    return value * factor

if __name__ == '__main__':
    sample_meters = 10
    feet_result = convert_unit(sample_meters, "meters_to_feet")
    print(feet_result)