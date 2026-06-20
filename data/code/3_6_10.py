class TemperatureSensor:
    def __init__(self, sensor_id, celsius_value):
        self.sensor_id = sensor_id
        self.celsius_value = celsius_value

    def convert_to_kelvin(self):
        return self.celsius_value + 273.15

    def __str__(self):
        return f"Sensor {self.sensor_id}: {self.celsius_value}°C, {self.convert_to_kelvin():.2f}K"

def display_temperature_table(sensors):
    print(f"{'ID':<10}{'Celsius':<15}{'Kelvin':<15}")
    print("-" * 40)
    for sensor in sensors:
        print(f"{sensor.sensor_id:<10}{sensor.celsius_value:<15}{sensor.convert_to_kelvin():.2f}")

def process_data():
    sensors = [
        TemperatureSensor("S001", 22.5),
        TemperatureSensor("S002", 18.3),
        TemperatureSensor("S003", 35.0),
        TemperatureSensor("S004", 0.0),
        TemperatureSensor("S005", -10.5),
    ]
    return sensors

if __name__ == '__main__':
    sensor_list = process_data()
    display_temperature_table(sensor_list)