def celsius_to_kelvin(celsius):
    return celsius + 273.15

def process_sensor_data(sensors):
    print(f"{'Sensor ID':<15} {'Temperature (°C)':<20} {'Temperature (K)':<20}")
    print("-" * 55)
    results = []
    for sensor_id, temp_celsius in sensors:
        temp_kelvin = celsius_to_kelvin(temp_celsius)
        print(f"{sensor_id:<15} {temp_celsius:<20.2f} {temp_kelvin:<20.2f}")
        results.append((sensor_id, temp_celsius, temp_kelvin))
    return results

if __name__ == '__main__':
    sample_sensors = [
        ("Sensor_A", 22.5),
        ("Sensor_B", -5.0),
        ("Sensor_C", 100.0),
        ("Sensor_D", 37.8),
        ("Sensor_E", 0.0)
    ]
    process_sensor_data(sample_sensors)