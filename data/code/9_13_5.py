from dataclasses import dataclass
from typing import Union

VOLUME_CONVERSIONS = {
    "ml_to_l": 0.001,
    "l_to_ml": 1000.0,
    "m3_to_l": 1000.0,
    "l_to_m3": 0.001,
    "gal_to_l": 3.78541,
    "l_to_gal": 0.264172,
}

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == "ml" and to_unit == "l":
        return value * VOLUME_CONVERSIONS["ml_to_l"]
    elif from_unit == "l" and to_unit == "ml":
        return value * VOLUME_CONVERSIONS["l_to_ml"]
    elif from_unit == "m3" and to_unit == "l":
        return value * VOLUME_CONVERSIONS["m3_to_l"]
    elif from_unit == "l" and to_unit == "m3":
        return value * VOLUME_CONVERSIONS["l_to_m3"]
    elif from_unit == "gal" and to_unit == "l":
        return value * VOLUME_CONVERSIONS["gal_to_l"]
    elif from_unit == "l" and to_unit == "gal":
        return value * VOLUME_CONVERSIONS["l_to_gal"]
    elif from_unit == "ml" and to_unit == "m3":
        return value * VOLUME_CONVERSIONS["ml_to_l"] * VOLUME_CONVERSIONS["l_to_m3"]
    elif from_unit == "m3" and to_unit == "ml":
        return value * VOLUME_CONVERSIONS["m3_to_l"] * VOLUME_CONVERSIONS["l_to_ml"]
    elif from_unit == "ml" and to_unit == "gal":
        return value * VOLUME_CONVERSIONS["ml_to_l"] * VOLUME_CONVERSIONS["l_to_gal"]
    elif from_unit == "gal" and to_unit == "ml":
        return value * VOLUME_CONVERSIONS["gal_to_l"] * VOLUME_CONVERSIONS["l_to_ml"]
    elif from_unit == "m3" and to_unit == "gal":
        return value * VOLUME_CONVERSIONS["m3_to_l"] * VOLUME_CONVERSIONS["l_to_gal"]
    elif from_unit == "gal" and to_unit == "m3":
        return value * VOLUME_CONVERSIONS["gal_to_l"] * VOLUME_CONVERSIONS["l_to_m3"]
    else:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    print(convert_volume(1000, "ml", "l"))
    print(convert_volume(1, "l", "ml"))
    print(convert_volume(1, "m3", "l"))
    print(convert_volume(1000, "l", "m3"))
    print(convert_volume(1, "gal", "l"))
    print(convert_volume(3.78541, "l", "gal"))
    print(convert_volume(1000, "ml", "m3"))
    print(convert_volume(0.001, "m3", "ml"))
    print(convert_volume(1000, "ml", "gal"))
    print(convert_volume(1, "gal", "ml"))
    print(convert_volume(1, "m3", "gal"))
    print(convert_volume(1, "gal", "m3"))