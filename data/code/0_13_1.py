import sys
def convert_length(value, unit):
    if unit == "km":
        if "m" in unit:
            return value * 1000
        elif "ft" in unit:
            return value * 3280.84
    return None
if __name__ == '__main__':
    measurements = [1.5, 10.0, 50.5, 100.0]
    unit = "km"
    print(f"--- Measurements in {unit.upper()} ---")
    for length_km in measurements:
        meters = convert_length(length_km, "m")
        feet = convert_length(length_km, "ft")
        if meters is not None and feet is not None:
            print(f"Original: {length_km:.2f} {unit}")
            print(f"Meters: {meters:.2f} m")
            print(f"Feet: {feet:.2f} ft")
        else:
            print(f"Error processing: {length_km} {unit}")
    print("---------------------------------")