class TemperatureSensor:
    def __init__(self, sensor_id, celsius_temp):
        self.sensor_id = sensor_id
        self.celsius_temp = celsius_temp

    def to_kelvin(self):
        return self.celsius_temp + 273.15

    def display(self):
        kelvin_temp = self.to_kelvin()
        print(f"{self.sensor_id:<10} {self.celsius_temp:<10.2f} {kelvin_temp:<10.2f}")

def create_sensors(sensor_data):
    sensors = []
    for sensor_id, celsius_temp in sensor_data.items():
        sensors.append(TemperatureSensor(sensor_id, celsius_temp))
    return sensors

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 30.5,
        'SensorB': -10.0,
        'SensorC': 20.0,
        'SensorD': 50.0
    }
    
    sensors = create_sensors(sample_sensor_data)
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    for sensor in sensors:
        sensor.display()