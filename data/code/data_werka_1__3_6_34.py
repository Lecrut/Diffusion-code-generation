class TemperatureSensor:
    def __init__(self, sensor_id, temperature_celsius):
        self.sensor_id = sensor_id
        self.temperature_celsius = temperature_celsius

    def to_kelvin(self):
        return self.temperature_celsius + 273.15

def display_temperatures(sensor_data):
    print(f"{'Sensor ID':<10} {'Temperature (C)':<20} {'Temperature (K)':<20}")
    for sensor in sensor_data:
        kelvin_temp = sensor.to_kelvin()
        print(f"{sensor.sensor_id:<10} {sensor.temperature_celsius:<20.2f} {kelvin_temp:<20.2f}")

if __name__ == '__main__':
    sensors = [
        TemperatureSensor("S001", 25.3),
        TemperatureSensor("S002", -5.0),
        TemperatureSensor("S003", 0.0),
        TemperatureSensor("S004", 100.0)
    ]
    display_temperatures(sensors)