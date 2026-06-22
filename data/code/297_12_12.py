class TemperatureConverter:
    FAHRENHEIT_TO_CELSIUS = 5/9
    CELSIUS_TO_FARENHEIT = 9/5
    FAHRENHEIT_OFFSET = -32
    CELSIUS_OFFSET = 0

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - TemperatureConverter.FAHRENHEIT_OFFSET) * TemperatureConverter.FAHRENHEIT_TO_CELSIUS + TemperatureConverter.CELSIUS_OFFSET

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius - TemperatureConverter.CELSIUS_OFFSET) * TemperatureConverter.CELSIUS_TO_FARENHEIT + TemperatureConverter.FAHRENHEIT_OFFSET

if __name__ == '__main__':
    fahrenheit_value = 100
    print(f"100F is {TemperatureConverter.fahrenheit_to_celsius(fahrenheit_value)}C")
    celsius_value = -40
    print(f"-40C is {TemperatureConverter.celsius_to_fahrenheit(celsius_value)}F")