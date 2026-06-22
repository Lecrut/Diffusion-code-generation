class TemperatureData:
    def __init__(self, sensor_id, celsius_temp):
        self.sensor_id = sensor_id
        self.celsius_temp = celsius_temp

    def to_kelvin(self):
        return self.celsius_temp + 273.15

def display_temperature_data(sensor_list):
    print(f"{'Sensor ID':<10} {'Celsius':<10} {'Kelvin':<10}")
    for sensor in sensor_list:
        try:
            if not isinstance(sensor, TemperatureData):
                raise ValueError("Invalid sensor object")
            kelvin_temp = sensor.to_kelvin()
            print(f"{sensor.sensor_id:<10} {sensor.celsius_temp:<10.2f} {kelvin_temp:<10.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    sample_sensors = [
        TemperatureData('SensorA', 23.5),
        TemperatureData('SensorB', -10.0),
        TemperatureData('SensorC', 37.0),
        TemperatureData('SensorD', 100.0)
    ]
    display_temperature_data(sample_sensors)