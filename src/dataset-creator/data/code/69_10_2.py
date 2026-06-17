from typing import Union
UNITS = ["kg", "g", "mg", "lb", "oz"]
TO_KG: dict[str, float] = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 1e-6,
    "lb": 0.45359237,
    "oz": 0.028349523125,
}
def convert_mass(value: float, from_unit: str, to_unit: str) -> Union[float, None]:
    if value < 0 or not isinstance(value, (int, float)):
        return None
    if from_unit not in UNITS or to_unit not in UNITS:
        return None
    factor_from_kg = TO_KG[from_unit]
    factor_to_kg = TO_KG[to_unit]
    kg_value = value * factor_from_kg / factor_to_kg
    return round(kg_value, 10) if isinstance(value, float) else int(round(kg_value))
if __name__ == '__main__':
    test_cases = [
        (5.0, "kg", "lb"),
        (100, "g", "mg"),
        (-5, "kg", "oz"),                             
        ("invalid", "kg", "g"),                                            
        (2.5, "xyz", "lb"),                                
    ]
    for val_str, u1, u2 in test_cases:
        try:
            value = float(val_str) if isinstance(val_str, str) else val_str
            result = convert_mass(value, u1, u2)
            print(f"Converted {value} from {u1} to {u2}: {result}")
        except Exception as e:
            print(f"Error processing input for {val_str}, {u1}, {u2}: {e}")