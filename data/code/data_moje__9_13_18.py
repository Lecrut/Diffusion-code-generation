from typing import Dict

CONVERSIONS_METRIC_TO_LITRE: Dict[str, float] = {
    "mL": 0.001,
    "L": 1.0,
    "m³": 1000.0,
}

CONVERSIONS_IMPERIAL_TO_LITRE: Dict[str, float] = {
    "gal": 3.78541,
}

UNIT_TO_TYPE: Dict[str, str] = {
    "mL": "metric",
    "L": "metric",
    "m³": "metric",
    "gal": "imperial",
}

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in UNIT_TO_TYPE:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in UNIT_TO_TYPE:
        raise ValueError(f"Unknown unit: {to_unit}")

    if from_unit == to_unit:
        return value

    if from_unit == "mL":
        litres = value * CONVERSIONS_METRIC_TO_LITRE["mL"]
    elif from_unit == "L":
        litres = value * CONVERSIONS_METRIC_TO_LITRE["L"]
    elif from_unit == "m³":
        litres = value * CONVERSIONS_METRIC_TO_LITRE["m³"]
    elif from_unit == "gal":
        litres = value * CONVERSIONS_IMPERIAL_TO_LITRE["gal"]
    else:
        raise ValueError(f"Cannot convert from {from_unit}")

    if to_unit == "mL":
        return litres / CONVERSIONS_METRIC_TO_LITRE["mL"]
    elif to_unit == "L":
        return litres / CONVERSIONS_METRIC_TO_LITRE["L"]
    elif to_unit == "m³":
        return litres / CONVERSIONS_METRIC_TO_LITRE["m³"]
    elif to_unit == "gal":
        return litres / CONVERSIONS_IMPERIAL_TO_LITRE["gal"]
    else:
        raise ValueError(f"Cannot convert to {to_unit}")

if __name__ == "__main__":
    result = convert_volume(1.0, "gal", "L")
    print(result)
    result2 = convert_volume(1000.0, "mL", "L")
    print(result2)
    result3 = convert_volume(1.0, "m³", "gal")
    print(result3)