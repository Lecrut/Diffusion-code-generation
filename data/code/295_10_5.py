import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def meters_to_feet(meters):
    return meters * 3.28084
def feet_to_meters(feet):
    return feet / 3.28084
def kilograms_to_pounds(kg):
    return kg * 2.20462
def pounds_to_kilograms(pounds):
    return pounds / 2.20462
def liters_to_gallons(liters):
    return liters * 0.264172
def gallons_to_liters(gallons):
    return gallons / 0.264172
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        if not isinstance(value, (int, float)):
            raise ValueError("Input value must be numeric for temperature conversion.")
        if from_unit == 'C':
            return celsius_to_fahrenheit(value)
        else:
            return fahrenheit_to_celsius(value)
    return None
def convert_length(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be numeric for length conversion.")
    if from_unit == 'm' and to_unit == 'ft':
        return meters_to_feet(value)
    elif from_unit == 'ft' and to_unit == 'm':
        return feet_to_meters(value)
    return None
def convert_weight(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be numeric for weight conversion.")
    if from_unit == 'kg' and to_unit == 'lb':
        return kilograms_to_pounds(value)
    elif from_unit == 'lb' and to_unit == 'kg':
        return pounds_to_kilograms(value)
    return None
def convert_volume(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be numeric for volume conversion.")
    if from_unit == 'L' and to_unit == 'gal':
        return liters_to_gallons(value)
    elif from_unit == 'gal' and to_unit == 'L':
        return gallons_to_liters(value)
    return None
if __name__ == '__main__':
    print("--- Temperature Conversion (C <-> F) ---")
    temp_c = 25.0
    temp_f = convert_temperature(temp_c, 'C', 'F')
    if temp_f is not None:
        print(f"{temp_c}°C is {temp_f:.2f}°F")
    print("\n--- Length Conversion (M <-> FT) ---")
    length_m = 10.0
    length_ft = convert_length(length_m, 'm', 'ft')
    if length_ft is not None:
        print(f"{length_m}m is {length_ft:.2f}ft")
    length_ft_val = 6.5
    length_m_val = convert_length(length_ft_val, 'ft', 'm')
    if length_m_val is not None:
        print(f"{length_ft_val}ft is {length_m_val:.2f}m")
    print("\n--- Weight Conversion (KG <-> LB) ---")
    weight_kg = 50.0
    weight_lb = convert_weight(weight_kg, 'kg', 'lb')
    if weight_lb is not None:
        print(f"{weight_kg}kg is {weight_lb:.2f}lb")
    weight_lb_val = 150.0
    weight_kg_val = convert_weight(weight_lb_val, 'lb', 'kg')
    if weight_kg_val is not None:
        print(f"{weight_lb_val}lb is {weight_kg_val:.2f}kg")
    print("\n--- Volume Conversion (L <-> GAL) ---")
    volume_l = 10.0
    volume_gal = convert_volume(volume_l, 'L', 'gal')
    if volume_gal is not None:
        print(f"{volume_l}L is {volume_gal:.2f}gal")
    volume_gal_val = 20.0
    volume_l_val = convert_volume(volume_gal_val, 'gal', 'L')
    if volume_l_val is not None:
        print(f"{volume_gal_val}gal is {volume_l_val:.2f}L")
    print("\n--- Input Validation Test ---")
    try:
        convert_length("ten", 'm', 'ft')
    except ValueError as e:
        print(f"Caught expected error for invalid input: {e}")
    try:
        convert_weight("abc", 'kg', 'lb')
    except ValueError as e:
        print(f"Caught expected error for invalid input: {e}")