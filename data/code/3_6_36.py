def read_temperature_data(sensor_inputs):
    results = []
    for sensor_id, celsius in sensor_inputs.items():
        kelvin = celsius + 273.15
        results.append((sensor_id, celsius, kelvin))
    return results

def display_temperature_table(results):
    print(f"{'Sensor ID':<10} {'Celsius':>8} {'Kelvin':>9}")
    print("-" * 30)
    for sensor_id, celsius, kelvin in results:
        print(f"{sensor_id:<10} {celsius:>8.2f} {kelvin:>9.2f}")

if __name__ == '__main__':
    sample_sensor_inputs = {
        'Sensor1': 25.3,
        'Sensor2': -5.0,
        'Sensor3': 0.0,
        'Sensor4': 37.0
    }
    
    results = read_temperature_data(sample_sensor_inputs)
    display_temperature_table(results)