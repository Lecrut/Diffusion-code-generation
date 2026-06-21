class TemperatureConverter:
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

def display_temperature_data(sensor_data):
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    for sensor_id, temp_c in sensor_data.items():
        try:
            if not isinstance(temp_c, (int, float)):
                raise ValueError("Temperature must be a number")
            temp_k = TemperatureConverter.celsius_to_kelvin(temp_c)
            print(f"{sensor_id:<10} {temp_c:<10.2f} {temp_k:<10.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    sample_sensor_data = {
        'SensorA': 30.5,
        'SensorB': -10.0,
        'SensorC': 200.0,
        'SensorD': 15.75
    }
    display_temperature_data(sample_sensor_data)