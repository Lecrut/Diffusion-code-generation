def convert_fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    return kelvin

def display_temperature_table(sensor_data):
    print(f"{'Sensor ID':<12} {'Temp (F)':<12} {'Temp (K)':<12}")
    print("-" * 36)
    for sensor_id, temp_f in sensor_data.items():
        temp_k = convert_fahrenheit_to_kelvin(temp_f)
        print(f"{sensor_id:<12} {temp_f:<12.2f} {temp_k:<12.2f}")

if __name__ == '__main__':
    sample_sensors = {
        "SENSOR_01": 32.0,
        "SENSOR_02": 75.5,
        "SENSOR_03": 98.6,
        "SENSOR_04": -40.0,
        "SENSOR_05": 212.0
    }
    display_temperature_table(sample_sensors)