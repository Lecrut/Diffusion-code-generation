import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

def format_table(temperatures_celsius: list[float]) -> None:
    """Display the temperature data in a formatted table including Kelvin conversion."""
    if not temperatures_celsius:
        print("No temperature data provided.")
        return

    max_len = len(str(max(abs(t) for t in temperatures_celsius))) + 1
    
    # Header
    header = f"{'Index':<{max_len}} | {'Celsius (°C)':>10} | {'Kelvin (K)':>12}"
    print(header.center(45))

    separator = "-" * len(header)
    print(separator)

    for i, c in enumerate(temperatures_celsius):
        k = celsius_to_kelvin(c)
        row = f"{i:>{max_len}} | {c:>10.2f} | {k:.3f}"
        print(row.center(45))

def main():
    # Hard-coded sample temperature data in Celsius
    sensor_data = [
        25.0,   # Room temperature
        -40.0,  # Freezing cold point (Celsius)
        100.0,  # Boiling water
        37.0,   # Human body temp approx
        -196.0  # Liquid nitrogen
    ]

    print("Temperature Sensor Data Report")
    print("=" * 45)
    
    format_table(sensor_data)

if __name__ == '__main__':
    main()