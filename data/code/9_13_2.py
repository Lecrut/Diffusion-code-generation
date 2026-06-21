from typing import Dict, Union

L_PER_GAL: float = 0.00378541
ML_PER_L: float = 1000.0
M3_PER_L: float = 0.001

CONVERSION_FACTORS: Dict[str, float] = {
    "mL": ML_PER_L,
    "L": 1.0,
    "gal": 1.0 / L_PER_GAL,
    "m³": 1.0 / M3_PER_L
}

TARGET_UNITS: Dict[str, str] = {
    "mL": "mL",
    "L": "L",
    "gal": "L",
    "m³": "L"
}

UNIT_TO_LITER: Dict[str, float] = {
    "mL": ML_PER_L,
    "L": 1.0,
    "gal": 1.0 / L_PER_GAL,
    "m³": 1.0 / M3_PER_L
}

UNIT_FROM_LITER: Dict[str, float] = {
    "mL": 1.0 / ML_PER_L,
    "L": 1.0,
    "gal": L_PER_GAL,
    "m³": M3_PER_L
}

def convert_volume(value: float, unit_from: str, unit_to: str) -> float:
    if unit_from not in UNIT_TO_LITER:
        raise ValueError(f"Unsupported source unit: {unit_from}")
    if unit_to not in UNIT_FROM_LITER:
        raise ValueError(f"Unsupported target unit: {unit_to}")
    
    liters = value * UNIT_TO_LITER[unit_from]
    result = liters * UNIT_FROM_LITER[unit_to]
    return result

def list_supported_units() -> list:
    return list(UNIT_TO_LITER.keys())

if __name__ == '__main__':
    val: float = 1.0
    src_unit: str = "gal"
    tgt_unit: str = "L"
    
    converted: float = convert_volume(val, src_unit, tgt_unit)
    print(converted)