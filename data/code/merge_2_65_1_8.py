def convert_length(meters: float) -> dict:
    km = meters / 1000.0
    cm = meters * 100.0
    mm = meters * 1000.0
    inch = inches_per_meter * meters
    foot = feet_per_meter * meters
    yard = yards_per_meter * meters
    mile = miles_per_meter * meters
    return {
        "km": km,
        "cm": cm,
        "mm": mm,
        "inch": inch,
        "foot": foot,
        "yard": yard,
        "mile": mile
    }
inches_per_meter = 39.3701
feet_per_meter = 3.28084
yards_per_meter = 1.09361
miles_per_meter = 0.000621371
if __name__ == '__main__':
    sample_meters = 5.5
    result = convert_length(sample_meters)
    print(result)