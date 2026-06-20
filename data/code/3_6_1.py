def convert_to_kelvin(celsius):
    return celsius + 273.15

def display_temperature_table(sensor_data):
    print("Sensor ID | Celsius | Kelvin")
    print("-" * 35)
    for sensor_id, temp_c in sensor_data:
        temp_k = convert_to_kelvin(temp_c)
        print(f"{sensor_id:>9} | {temp_c:>7.2f} | {temp_k:>6.2f}")

if __name__ == '__main__':
    sensors = [
        ("TEMP_01", 22.5),
        ("TEMP_02", -5.0),
        ("TEMP_03", 100.0),
        ("TEMP_04", 37.8),
        ("TEMP_05", 0.0)
    ]
    display_temperature_table(sensors)