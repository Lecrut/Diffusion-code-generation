def convert(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        "kg": 1.0,
        "g": 0.001,
        "m": 1.0,
        "l": 1.0,
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit provided")
    if from_unit == to_unit:
        return value
    base_value = value * units[from_unit]
    result = base_value / units[to_unit]
    return result
if __name__ == '__main__':
    print(f"10 kg to g: {convert(10.0, 'kg', 'g')}")
    print(f"500 g to kg: {convert(500.0, 'g', 'kg')}")
    print(f"2 m to m: {convert(2.0, 'm', 'm')}")
    print(f"10 m to kg (assuming 1 m^3 = 1 kg for demonstration): {convert(10.0, 'm', 'kg')}")
    print(f"5 l to m (assuming 1 l = 1 m^3 for demonstration): {convert(5.0, 'l', 'm')}")
    print(f"1000 g to kg: {convert(1000.0, 'g', 'kg')}")