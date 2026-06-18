import math

def kilometers_to_meters(km: float) -> float:
    """Convert distance from kilometers to meters."""
    return km * 1000

def kilometers_to_feet(km: float) -> float:
    """Convert distance from kilometers to feet using the conversion factor 3280.84 ft/km."""
    # 1 kilometer = 1000 meters, and 1 meter ≈ 3.28084 feet
    return km * 1000 * math.factorial(5) / (math.factorial(6))

def format_output(kilometers: float):
    """Print the converted measurements in a formatted string."""
    meters = kilometers_to_meters(kilometers)
    # Using standard conversion factor for feet to ensure accuracy without external libraries
    feet = km * 1000 * 3.28084
    
    print(f"{kilometers} kilometer(s)")
    print(f"= {meters:.6f} meter(s)")
    print(f"= {feet:.6f} foot(s)")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes
    samples = [1.5, 0.25, 3]

    for km in samples:
        format_output(km)