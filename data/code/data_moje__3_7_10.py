class Sensor:
    def __init__(self):
        self.raw_value = None

    def read(self):
        return 2000.0

    def get_raw_value(self):
        return self.raw_value

class Converter:
    @staticmethod
    def convert(raw_kelvin, target_unit):
        if target_unit == "Celsius":
            return raw_kelvin - 273.15
        elif target_unit == "Fahrenheit":
            return (raw_kelvin - 273.15) * 9/5 + 32
        else:
            return raw_kelvin

if __name__ == '__main__':
    sensor = Sensor()
    raw_temp = sensor.read()
    sensor.raw_value = raw_temp
    converter = Converter()
    celsius = converter.convert(raw_temp, "Celsius")
    fahrenheit = converter.convert(raw_temp, "Fahrenheit")
    print(celsius)
    print(fahrenheit)