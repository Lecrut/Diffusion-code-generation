class TemperatureSensor:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def get_kelvin(self):
        return self.celsius + 273.15

def simulate_readings(sensors):
    print(f"{'Sensor ID':<12} {'Celsius':<10} {'Kelvin':<10}")
    print("-" * 34)
    results = []
    for i, celsius in enumerate(sensors):
        sensor = TemperatureSensor(celsius)
        kelvin = sensor.get_kelvin()
        print(f"Sensor {i:<6} {sensor.celsius:<10.2f} {kelvin:<10.2f}")
        results.append((i, sensor.celsius, kelvin))
    return results

if __name__ == '__main__':
    sample_data = [20.5, -5.0, 100.0, 37.3, 0.0]
    simulate_readings(sample_data)