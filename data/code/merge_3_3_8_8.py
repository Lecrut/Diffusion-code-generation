import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

class TemperatureSensorSimulator:
    def __init__(self):
        self.sensor_data = [
            {"id": "SENS-001", "location": "North Hall", "celsius": -4.5},
            {"id": "SENS-002", "location": "South Wing", "celsius": 22.3},
            {"id": "SENS-003", "location": "Server Room A", "celsius": 18.7},
            {"id": "SENS-004", "location": "Lab Alpha", "celsius": -12.0},
            {"id": "SENS-005", "location": "Greenhouse B", "celsius": 35.6}
        ]

    def display_results(self):
        """Display the temperature data in a formatted table."""
        print(f"{'ID':<12} | {'Location':<18} | {'Celsius (°C)':>10} | {'Kelvin (K)':>14}")
        print("-" * 65)

        for sensor in self.sensor_data:
            kelvin_temp = celsius_to_kelvin(sensor["celsius"])
            row_str = f"{sensor['id']:<12} | {sensor['location']:<18} | {sensor['celsius']:>10.1f} | {kelvin_temp:>14.2f}"
            print(row_str)

if __name__ == '__main__':
    simulator = TemperatureSensorSimulator()
    simulator.display_results()