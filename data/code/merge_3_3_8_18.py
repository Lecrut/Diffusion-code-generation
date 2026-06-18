import math

def celsius_to_kelvin(celsius):
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

# Predefined set of sensor input data (Celsius)
SENSOR_DATA = [
    {"id": "SN001", "location": "North Zone", "value_c": -40},
    {"id": "SN002", "location": "Central Hall", "value_c": 25.5},
    {"id": "SN003", "location": "South Garden", "value_c": 87.1},
    {"id": "SN004", "location": "East Server Room", "value_c": -196},
    {"id": "SN005", "location": "West Lab", "value_c": 32}
]

def format_table(data):
    """Format the sensor data into a readable table."""
    if not data:
        return []
    
    # Determine column widths based on content length
    max_id_len = len(max(item['id'], key=len)) + 10
    max_loc_len = len(max(item['location'], key=len)) + 25
    
    rows = [["ID", "Location", "Temp (°C)", "Temp (K)"]]
    
    for item in data:
        kelvin_value = celsius_to_kelvin(item['value_c'])
        
        # Format values with alignment considerations

if __name__ == '__main__':
    pass
