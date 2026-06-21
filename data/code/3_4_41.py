class TemperatureData:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def validate_sensor_data(self):
        if not isinstance(self.sensor_data, dict):
            raise ValueError("Sensor data must be a dictionary")
        for key, value in self.sensor_data.items():
            if not isinstance(key, str) or not isinstance(value, (int, float)):
                raise ValueError("Invalid sensor ID or temperature value")

    def convert_to_kelvin(self, celsius):
        return celsius + 273.15

    def display_temperature_data(self):
        self.validate_sensor_data()
        print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
        for sensor_id, temp_c in self.sensor_data.items():
            temp_k = self.convert_to_kelvin(temp_c)
            print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 25.3,
        'SensorB': -5.0,
        'SensorC': 0.0,
        'SensorD': 100.0
    }
    temp_data = TemperatureData(sample_sensor_data)
    temp_data.display_temperature_data()