def celsius_to_kelvin(celsius):
    return celsius + 273.15

def read_sensor_data(sensor_values):
    results = []
    for name, celsius in sensor_values.items():
        kelvin = celsius_to_kelvin(celsius)
        results.append((name, celsius, kelvin))
    return results

def display_table(rows):
    print(f"{'Sensor':<15} {'Celsius':>10} {'Kelvin':>10}")
    print("-" * 35)
    for name, celsius, kelvin in rows:
        print(f"{name:<15} {celsius:>10.2f} {kelvin:>10.2f}")

if __name__ == '__main__':
    sensor_inputs = {
        "Sensor A": 25.0,
        "Sensor B": 100.0,
        "Sensor C": -40.0
    }
    
    data = read_sensor_data(sensor_inputs)
    display_table(data)