def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        "mL": 1e-3,
        "L": 1.0,
        "m3": 1000.0,
        "gal": 3.78541
    }
    if from_unit not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    liters = value * units[from_unit]
    result = liters / units[to_unit]
    return result

def ml_to_l(ml: float) -> float:
    return convert_volume(ml, "mL", "L")

def l_to_ml(liters: float) -> float:
    return convert_volume(liters, "L", "mL")

def l_to_m3(liters: float) -> float:
    return convert_volume(liters, "L", "m3")

def m3_to_l(m3: float) -> float:
    return convert_volume(m3, "m3", "L")

def l_to_gal(liters: float) -> float:
    return convert_volume(liters, "L", "gal")

def gal_to_l(gallons: float) -> float:
    return convert_volume(gallons, "gal", "L")

if __name__ == '__main__':
    print(ml_to_l(500.0))
    print(l_to_ml(2.5))
    print(l_to_m3(100.0))
    print(m3_to_l(0.5))
    print(l_to_gal(1.0))
    print(gal_to_l(1.0))
    print(convert_volume(1000.0, "mL", "gal"))