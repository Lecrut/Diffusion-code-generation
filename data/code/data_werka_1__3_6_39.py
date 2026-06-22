def celsius_to_kelvin(celsius):
    return celsius + 273.15

def display_temperature_table(temperatures):
    print("Temperature Data")
    print(f"{'Sensor':<10} {'Celsius':>10} {'Kelvin':>10}")
    for sensor, celsius in temperatures.items():
        kelvin = celsius_to_kelvin(celsius)
        print(f"{sensor:<10} {celsius:>10.2f} {kelvin:>10.2f}")

if __name__ == '__main__':
    sample_temperatures = {
        'Sensor1': 25.0,
        'Sensor2': 30.5,
        'Sensor3': 18.7,
        'Sensor4': -5.0
    }
    display_temperature_table(sample_temperatures)