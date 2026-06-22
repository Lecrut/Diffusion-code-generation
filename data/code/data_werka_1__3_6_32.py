class TemperatureSensorData:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def convert_to_kelvin(self, celsius):
        return celsius + 273.15

    def display_temperatures(self):
        print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
        for sensor_id, temp_c in self.sensor_data.items():
            temp_k = self.convert_to_kelvin(temp_c)
            print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'Sensor_001': 25.3,
        'Sensor_002': -5.0,
        'Sensor_003': 0.0,
        'Sensor_004': 37.5
    }
    sensor_data_instance = TemperatureSensorData(sample_sensor_data)
    sensor_data_instance.display_temperatures()