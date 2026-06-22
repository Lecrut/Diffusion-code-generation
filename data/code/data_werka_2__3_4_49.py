def celsius_to_kelvin(celsius):
    return celsius + 273.15

def format_temperature_data(sensor_data):
    print("Sensor ID | Temperature (C) | Temperature (K)")
    print("-------------------------------------------")
    for sensor_id, temp_c in sensor_data.items():
        temp_k = celsius_to_kelvin(temp_c)
        print(f"   {sensor_id:7} |     {temp_c:13.2f} |     {temp_k:13.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'S001': 25.3,
        'S002': -5.6,
        'S003': 0.0,
        'S004': 100.0
    }
    format_temperature_data(sample_sensor_data)