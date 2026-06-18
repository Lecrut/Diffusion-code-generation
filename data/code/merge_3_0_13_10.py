import math

def convert_kilometers_to_meters(km: float) -> float:
    """Convert kilometers to meters."""
    return km * 1000

def convert_meters_to_feet(meters: float) -> float:
    """Convert meters to feet using the standard conversion factor (1 meter = 3.28084 feet)."""
    return meters * 3.28084

def process_measurements(measurements_km: list[float]) -> None:
    """Process a list of kilometer measurements and print equivalents in meters and feet."""
    for i, km_val in enumerate(measurements_km):
        meters = convert_kilometers_to_meters(km_val)
        feet = convert_meters_to_feet(meters)

        # Print formatted output with 2 decimal places
        print(f"Measurement {i + 1}:")
        print(f"  Kilometers: {km_val:.4f} km")
        print(f"  Meters:     {meters:.4f} m")
        print(f"  Feet:       {feet:.2f} ft")

if __name__ == '__main__':
    # Hard-coded sample values in kilometers as per task requirement
    sample_data = [1.5, 0.75, -0.3]

    process_measurements(sample_data)