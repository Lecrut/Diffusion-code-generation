class TemperatureData:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def display_temperature_data(self):
        print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
        for sensor_id, temp_c in self.sensor_data.items():
            temp_k = self.celsius_to_kelvin(temp_c)
            print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 30.5,
        'SensorB': -10.0,
        'SensorC': 50.0,
        'SensorD': 15.7
    }
    temperature_data = TemperatureData(sample_sensor_data)
    temperature_data.display_temperature_data()