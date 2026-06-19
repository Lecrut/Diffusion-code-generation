class TemperatureSensorData:

    def __init__(self, sensor_id, temperature_celsius):
        self.sensor_id = sensor_id
        self.temperature_celsius = temperature_celsius

    def to_kelvin(self):
        return self.temperature_celsius + 273.15

def display_temperature_data(sensor_data_list):
    print('Sensor ID | Temp (C) | Temp (K)')
    print('-----------------------------')
    for data in sensor_data_list:
        kelvin_temp = data.to_kelvin()
        print(f'{data.sensor_id:9} | {data.temperature_celsius:8.2f} | {kelvin_temp:8.2f}')
if __name__ == '__main__':
    sensors = [TemperatureSensorData(1, 25.0), TemperatureSensorData(2, -5.0), TemperatureSensorData(3, 0.0), TemperatureSensorData(4, 100.0)]
    display_temperature_data(sensors)