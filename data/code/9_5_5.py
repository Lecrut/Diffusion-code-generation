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
    elif unit.lower() == "us_gal":
        return volume * 3.785411784
    elif unit.lower() == "gallon":
        return volume * 3.785411784
    elif unit.lower() == "qt":
        return volume * 0.946352946
    elif unit.lower() == "pint":
        return volume * 0.473176473
    elif unit.lower() == "fl_oz":
        return volume * 0.0295735295625
    elif unit.lower() == "ounce":
        return volume * 0.028349523
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    sample_volume_1 = 1.0
    sample_unit_1 = "liter"
    result_1 = convert_to_liters(sample_volume_1, sample_unit_1)
    print(f"Volume: {sample_volume_1} {sample_unit_1} -> Liters: {result_1}")
    sample_volume_2 = 10.0
    sample_unit_2 = "gallon"
    result_2 = convert_to_liters(sample_volume_2, sample_unit_2)
    print(f"Volume: {sample_volume_2} {sample_unit_2} -> Liters: {result_2}")
    sample_volume_3 = 500.0
    sample_unit_3 = "milliliter"
    result_3 = convert_to_liters(sample_volume_3, sample_unit_3)
    print(f"Volume: {sample_volume_3} {sample_unit_3} -> Liters: {result_3}")
    sample_volume_4 = 100.0
    sample_unit_4 = "cm3"
    result_4 = convert_to_liters(sample_volume_4, sample_unit_4)
    print(f"Volume: {sample_volume_4} {sample_unit_4} -> Liters: {result_4}")
    sample_volume_5 = 1.0
    sample_unit_5 = "us_gal"
    result_5 = convert_to_liters(sample_volume_5, sample_unit_5)
    print(f"Volume: {sample_volume_5} {sample_unit_5} -> Liters: {result_5}")
    sample_volume_6 = 1.0
    sample_unit_6 = "pint"
    result_6 = convert_to_liters(sample_volume_6, sample_unit_6)
    print(f"Volume: {sample_volume_6} {sample_unit_6} -> Liters: {result_6}")
    sample_volume_7 = 10.0
    sample_unit_7 = "ounce"
    result_7 = convert_to_liters(sample_volume_7, sample_unit_7)
    print(f"Volume: {sample_volume_7} {sample_unit_7} -> Liters: {result_7}")
    try:
        convert_to_liters(5.0, "furlong")
    except ValueError as e:
        print(f"Error caught: {e}")