def convert_metric_to_imperial(value, unit_type):
    if unit_type == "length":
        return value * 3.28084
    elif unit_type == "mass":
        return value * 2.20462
    elif unit_type == "volume":
        return value * 0.264172
    else:
        return None
if __name__ == '__main__':
    length_meters = 10
    length_imperial = convert_metric_to_imperial(length_meters, "length")
    print(f"Length conversion: {length_meters} meters is {length_imperial} feet")
    mass_kg = 50
    mass_imperial = convert_metric_to_imperial(mass_kg, "mass")
    print(f"Mass conversion: {mass_kg} kilograms is {mass_imperial} pounds")
    volume_liters = 10
    volume_imperial = convert_metric_to_imperial(volume_liters, "volume")
    print(f"Volume conversion: {volume_liters} liters is {volume_imperial} gallons")