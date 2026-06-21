class TemperatureData:
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def celsius_to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be a number")
        return celsius + 273.15

    def display(self):
        print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
        for sensor_id, temp_c in self.sensor_data.items():
            try:
                temp_k = self.celsius_to_kelvin(temp_c)
                print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")
            except ValueError as e:
                print(f"Error processing sensor {sensor_id}: {e}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 30.5,
        'SensorB': -10.0,
        'SensorC': 273.15,
        'SensorD': 100.0
    }
    temp_data = TemperatureData(sample_sensor_data)
    temp_data.display()