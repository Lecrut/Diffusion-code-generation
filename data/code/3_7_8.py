class Sensor:
    def __init__(self, raw_temp, unit='celsius'):
        self.raw_temp = raw_temp
        self.unit = unit

    def read_temperature(self):
        return self.raw_temp

class Converter:
    def __init__(self, sensor_instance):
        self.sensor = sensor_instance

    def convert_to_fahrenheit(self):
        if self.sensor.unit == 'celsius':
            return (self.sensor.raw_temp * 9/5) + 32
        elif self.sensor.unit == 'fahrenheit':
            return self.sensor.raw_temp
        else:
            raise ValueError("Unsupported unit")

    def convert_to_kelvin(self):
        if self.sensor.unit == 'celsius':
            return self.sensor.raw_temp + 273.15
        elif self.sensor.unit == 'fahrenheit':
            return (self.sensor.raw_temp - 32) * 5/9 + 273.15
        else:
            raise ValueError("Unsupported unit")

if __name__ == '__main__':
    sensor = Sensor(25, 'celsius')
    converter = Converter(sensor)
    print(converter.convert_to_fahrenheit())
    print(converter.convert_to_kelvin())