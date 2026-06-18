import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

def format_table(data):
    """Print the data in a neatly formatted table with headers and conversion results."""
    print(f"{'Index':<6} | {'Celsius (°C)':<14} | {'Kelvin (K)':<14}")
    print("-" * 50)
    
    for i, celsius in enumerate(data):
        kelvin = celsius_to_kelvin(celsius)
        # Format numbers to remove unnecessary trailing zeros but keep one decimal place if needed
        formatted_c = f"{celsius:.1f}"
        formatted_k = f"{kelvin:.2f}"
        
        print(f"{i:<6} | {formatted_c:<14} | {formatted_k:<14}")

if __name__ == '__main__':
    # Hard-coded sample temperature data in Celsius
    sensor_data = [
        0.0,      # Freezing point of water
        -273.15, # Absolute zero (approx)
        25.5,     # Room temperature approximation
        100.0,    # Boiling point of water at sea level
        40.8       # Body temperature average
    ]

    print("Temperature Sensor Data Report")
    format_table(sensor_data)