import math

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

class TemperatureSensorData:
    def __init__(self, sensor_id: int, location: str, readings_celsius: list):
        self.sensor_id = sensor_id
        self.location = location
        self.readings_celsius = readings_celsius
    
    @property
    def converted_readings(self) -> list[float]:
        return [celsius_to_kelvin(temp) for temp in self.readings_celsius]

def format_table(data_list: list[TemperatureSensorData]) -> str:
    """Format the sensor data into a neat table."""
    if not data_list:
        return "No data available."
    
    # Calculate column widths based on content to ensure alignment
    header = f"{'ID':<4} | {'Location':<15} | {'Celsius (°C)':>8} | {'Kelvin (K)':>9}"
    max_id_width = len(str(max(d.sensor_id for d in data_list))) if data_list else 0
    
    # Determine width based on actual content to ensure neatness, 
    # but keep it simple and fixed-width enough for typical cases.
    lines = [header]
    
    for sensor_data in data_list:
        row_parts = []
        
        # ID column (right aligned)
        id_str = f"{sensor_data.sensor_id:>4}"
        row_parts.append(id_str)
        
        # Location column (left padded to match header width roughly, or just left align with padding)
        loc_str = sensor_data.location.ljust(15)[:20]  # Truncate if too long for neatness
        row_parts.append(loc_str[:14])  # Match the visual block
        
        # Celsius column (right aligned)
        celsius_row = [f"{temp:.2f}" for temp in sensor_data.readings_celsius]
        
        # Kelvin column (left padded to match header width roughly, or just left align with padding)
        kelvin_row = [str(temp)[:10].ljust(9) if len(str(temp)) <= 8 else str(temp).rjust(9) for temp in sensor_data.converted_readings]

    # Construct the table rows dynamically to ensure neatness regardless of data length
    result_lines = []
    
    # Header line construction with dynamic widths based on max values found or fixed reasonable width
    header_parts = [f"{sensor_id:<4}" if isinstance(sensor_id, int) else str(sensor_id), 
                   f"{'Location':<15}", "Celsius (°C)", "Kelvin (K)"]
    
    # Re-evaluating for a truly neat table that handles variable data gracefully without complex dynamic width calculation which might be overkill.
    # We will use fixed column widths that are sufficient and visually aligned.
    
    lines = []
    header_line = f"{'ID':<4} | {'Location':<15} | {'Celsius (°C)':>8} | {'Kelvin (K)':>9}"
    lines.append(header_line)
    
    for sensor in data_list:
        row_parts = [f"{sensor.sensor_id:<4}", f"{sensor.location.ljust(12)}", 
                    *[f"{c:.2f}" for c in sensor.readings_celsius], 
                    *[str(k)[:8].ljust(9) if len(str(k)) <= 7 else str(k).rjust(9) for k in sensor.converted_readings]]
        
        # Construct the row string carefully to match header alignment roughly
        row_str = f"{sensor.sensor_id:<4} | {sensor.location.ljust(12)} | " + \
                  ", ".join(f"{c:.2f}" for c in sensor.readings_celsius) + " | " + \
                  ", ".join(str(k)[:8].ljust(9) if len(str(k)) <= 7 else str(k).rjust(9) for k in sensor.converted_readings)
        lines.append(row_str)

    return "\n".join(lines)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    
    sensors = [
        TemperatureSensorData(101, "Main Hall", [-5.2, 22.8, 36.4]),
        TemperatureSensorData(102, "Server Room A", [18.5, 19.0, 20.1]),
        TemperatureSensorData(103, "Outdoor North", [-12.7, -8.3, -2.1])
    ]

    print(format_table(sensors))