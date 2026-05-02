class TemperatureConverter:
    def convert_all(self, celsius_readings):
        fahrenheit_readings = []
        for celsius in celsius_readings:
            fahrenheit = (celsius * 9/5) + 32
            fahrenheit_readings.append(fahrenheit)
        return fahrenheit_readings
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_temps = [0, 10, 20, 25, 30]
    fahrenheit_temps = converter.convert_all(celsius_temps)
    print(fahrenheit_temps)