import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

def format_table(temperature_data):
    """Print a neatly formatted table of temperatures and their Kelvin equivalents."""
    print(f"{'Index':<6} {'Celsius (°C)':<14} {'Kelvin (K)':<14}")
    print("-" * 38)

    for idx, c in enumerate(temperature_data):
        k = celsius_to_kelvin(c)
        # Format to ensure consistent decimal places and alignment
        print(f"{idx:<6} {c:>10.2f}   {k:>10.2f}")

def main():
    """Main function containing hard-coded sample sensor data."""
    # Predefined set of temperature readings in Celsius
    raw_temperatures = [
        25.5,
        -40.0,
        87.3,
        -196.1,
        0.0
    ]

    print("Temperature Data Simulation")
    print("=" * 38)
    
    # Process and display data in a table
    format_table(raw_temperatures)
    
    print("-" * 38)
    print(f"Total readings processed: {len(raw_temperatures)}")

if __name__ == '__main__':
    main()