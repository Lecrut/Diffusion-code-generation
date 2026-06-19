def convert_to_kelvin(celsius):
    return celsius + 273.15

def display_temperatures(sensor_data):
    print("Sensor ID | Temperature (C) | Temperature (K)")
    print("---------------------------------------------")
    for sensor_id, temp_c in sensor_data.items():
        temp_k = convert_to_kelvin(temp_c)
        print(f"   {sensor_id:7} |     {temp_c:12.2f} |     {temp_k:12.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        101: 25.3,
        102: -5.0,
        103: 15.8,
        104: 0.0
    }
    display_temperatures(sample_sensor_data)