class Sensor:
    def __init__(self, raw_value):
        self.raw_value = raw_value

    def get_raw_value(self):
        return self.raw_value

class Converter:
    C_OFFSET = 273.15

    @staticmethod
    def raw_to_celsius(raw_value):
        return raw_value - 273.15

    @staticmethod
    def celsius_to_fahrenheit(celsius_value):
        return celsius_value * 9 / 5 + 32

    @staticmethod
    def celsius_to_kelvin(celsius_value):
        return celsius_value + 273.15

if __name__ == '__main__':
    sensor = Sensor(300.15)
    raw = sensor.get_raw_value()
    celsius = Converter.raw_to_celsius(raw)
    fahrenheit = Converter.celsius_to_fahrenheit(celsius)
    kelvin = Converter.celsius_to_kelvin(celsius)
    print(f"{celsius=}")
    print(f"{fahrenheit=}")
    print(f"{kelvin=}")