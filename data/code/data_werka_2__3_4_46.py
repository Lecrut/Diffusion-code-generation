def celsius_to_kelvin(celsius):
    return celsius + 273.15

def display_temperature_data(sensor_data):
    print("Sensor ID | Temperature (C) | Temperature (K)")
    print("--------------------------------------------")
    for sensor_id, temp_c in sensor_data.items():
        temp_k = celsius_to_kelvin(temp_c)
        print(f"   {sensor_id}     |      {temp_c:.2f}       |      {temp_k:.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'S001': 25.3,
        'S002': -5.0,
        'S003': 37.8,
        'S004': 0.0
    }
    display_temperature_data(sample_sensor_data)