import math

def kilometers_to_meters(km: float) -> float:
    """Convert kilometers to meters."""
    return km * 1000

def kilometers_to_feet(km: float) -> float:
    """Convert kilometers to feet using the conversion factor (1 km = 3280.84 ft)."""
    return km * 3280.84

if __name__ == '__main__':
    # Sample data in kilometers with comments explaining the format and values
    measurements_km: list[float] = [
        5.0,   # Five kilometers
        1.75,  # One point seven five kilometers
        3280.84 / 1000  # Precisely one kilometer (to test exact conversion logic)
    ]

    for km in measurements_km:
        meters = kilometers_to_meters(km)
        feet = kilometers_to_feet(km)
        
        print(f"Input ({km} kilometers):")
        print(f"Meters: {meters:.2f}")
        print("Feet: {0:.2f}".format(feet))  # Pythonic string formatting for consistency