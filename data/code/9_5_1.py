import math
def convert_to_liters(volume: float, unit: str) -> float:
    if unit.lower() == "liter":
        return volume
    elif unit.lower() == "l":
        return volume
    elif unit.lower() == "ml":
        return volume / 1000.0
    elif unit.lower() == "milliliter":
        return volume / 1000.0
    elif unit.lower() == "cm3":
        return volume * 0.001
    elif unit.lower() == "cc":
        return volume * 0.001
    elif unit.lower() == "m3":
        return volume * 1000.0
    elif unit.lower() == "cubic meter":
        return volume * 1000.0
    elif unit.lower() == "cubic meter":
        return volume * 1000.0
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    volume_in_liters = 5.0
    unit1 = "liter"
    result1 = convert_to_liters(volume_in_liters, unit1)
    print(f"Input: {volume_in_liters} {unit1} -> Output: {result1} liters")
    volume_in_ml = 2500.0
    unit2 = "ml"
    result2 = convert_to_liters(volume_in_ml, unit2)
    print(f"Input: {volume_in_ml} {unit2} -> Output: {result2} liters")
    volume_in_cc = 1500.0
    unit3 = "cc"
    result3 = convert_to_liters(volume_in_cc, unit3)
    print(f"Input: {volume_in_cc} {unit3} -> Output: {result3} liters")
    volume_in_cm3 = 500.0
    unit4 = "cm3"
    result4 = convert_to_liters(volume_in_cm3, unit4)
    print(f"Input: {volume_in_cm3} {unit4} -> Output: {result4} liters")
    volume_in_m3 = 0.5
    unit5 = "m3"
    result5 = convert_to_liters(volume_in_m3, unit5)
    print(f"Input: {volume_in_m3} {unit5} -> Output: {result5} liters")
    try:
        convert_to_liters(10.0, "gallon")
    except ValueError as e:
        print(f"Error caught: {e}")