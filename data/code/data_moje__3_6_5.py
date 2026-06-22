def get_celsius_to_kelvin(celsius):
    return celsius + 273.15

def read_sensor_data(sensors):
    results = []
    for sensor_name, celsius_temp in sensors:
        kelvin_temp = get_celsius_to_kelvin(celsius_temp)
        results.append((sensor_name, celsius_temp, kelvin_temp))
    return results

def display_temperature_table(data):
    print(f"{'Sensor':<15} {'Celsius':<10} {'Kelvin':<10}")
    print("-" * 35)
    for name, celsius, kelvin in data:
        print(f"{name:<15} {celsius:<10.2f} {kelvin:<10.2f}")

if __name__ == '__main__':
    sensor_data = [
        ("Thermostat_A", 22.5),
        ("Server_Rack", 45.0),
        ("Outdoor_Prototype", -15.3),
        ("Incubator_B", 37.2),
        ("Cryo_Chamber", -196.0)
    ]
    processed_data = read_sensor_data(sensor_data)
    display_temperature_table(processed_data)