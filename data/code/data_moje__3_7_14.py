class Sensor:
    def read_raw_temperature(self, sensor_id):
        return 75.0

class Converter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

def main():
    sensor = Sensor()
    converter = Converter()

    raw_temp = sensor.read_raw_temperature("sensor_01")

    fahrenheit = converter.celsius_to_fahrenheit(raw_temp)
    kelvin = converter.celsius_to_kelvin(raw_temp)

    print(fahrenheit)
    print(kelvin)

if __name__ == '__main__':
    main()