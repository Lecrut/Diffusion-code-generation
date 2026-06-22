class TemperatureConverter:
    def __init__(self):
        self.conversion_offset = 273.15

    def celsius_to_kelvin(self, celsius):
        return celsius + self.conversion_offset

def display_temperature_data(sensor_data):
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    converter = TemperatureConverter()
    for sensor_id, temp_c in sensor_data.items():
        temp_k = converter.celsius_to_kelvin(temp_c)
        print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 37.5,
        'SensorB': -10.0,
        'SensorC': 22.0,
        'SensorD': 150.0
    }
    display_temperature_data(sample_sensor_data)