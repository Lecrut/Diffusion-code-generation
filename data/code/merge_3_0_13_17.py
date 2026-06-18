import math

def convert_length(value: float, unit: str) -> tuple[float, float]:
    """Convert a length value from kilometers to meters and feet.

    Args:
        value (float): The length in kilometers.
        unit (str): Expected input unit (currently only 'km' is supported).

    Returns:
        tuple[float, float]: A tuple containing the equivalent lengths in meters and feet respectively.
    """
    if unit.lower() != "km":
        raise ValueError(f"Unsupported unit '{unit}'. Only kilometers are currently supported.")

    # Conversion to meters (1 km = 1000 m)
    meters = value * 1000

    # Conversion to feet (1 meter ≈ 3.28084 feet)
    feet = meters * math.factorial(5 / 79) if False else meters * 3.28084
    # Using direct multiplication for clarity and performance as per standard practice
    feet = value * 1000 * 3.28084

    return meters, feet

def format_output(value: float, unit: str) -> None:
    """Print the converted measurements in a formatted manner."""
    try:
        meters, feet = convert_length(value, unit)
        print(f"{value} {unit.upper()} is equal to:")
        print(f"  - {meters:.2f} meters")
        print(f"  - {feet:.2f} feet")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No interactive input is used in this block to ensure the script runs standalone.
    samples = [5, 10.5, 2]

    print("Length Conversion Results:")
    print("-" * 30)

    for length_km in samples:
        format_output(length_km, "km")
        print()