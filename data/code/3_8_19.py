"""
Temperature Data Simulation Program

This module simulates reading temperature data from a set of predefined sensor inputs,
converts each value to Kelvin, and displays the results in a neatly formatted table.
No user interaction or external input is required.
"""

def convert_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

if __name__ == '__main__':
    # Hard-coded sample sensor data (Celsius)
    # Format: ['sensor_id', 'location', 'temperature_c']
    raw_data = [
        ["Sensor_001", "Server_Rack_A", 24.5],
        ["Sensor_002", "Database_Node_3", 28.1],
        ["Sensor_003", "Cooling_Unit_X", 26.7],
        ["Sensor_004", "Entry_Door_Elevators", 22.9],
    ]

    # Process data and prepare for display
    header = [
        f"{'ID':<15}", 
        f"{'Location':<35}", 
        f"{'Temp (°C)':>8}", 
        f"{'Temp (K)':>12}"
    ]