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
    feet = convert_metric_to_imperial(length_meters, "length")
    print(f"{length_meters} meters is {feet:.2f} feet")
    mass_kg = 75
    pounds = convert_metric_to_imperial(mass_kg, "mass")
    print(f"{mass_kg} kg is {pounds:.2f} pounds")
    volume_liters = 10
    gallons = convert_metric_to_imperial(volume_liters, "volume")
    print(f"{volume_liters} liters is {gallons:.2f} gallons")