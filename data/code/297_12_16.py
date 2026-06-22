class TemperatureConverter:
    FAHRENHEIT_TO_CELSIUS = 5/9
    CELSIUS_TO_FAHRENHEIT = 9/5

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * TemperatureConverter.FAHRENHEIT_TO_CELSIUS

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * TemperatureConverter.CELSIUS_TO_FAHRENHEIT + 32

if __name__ == '__main__':
    fahrenheit_value = -40
    celsius_value = 100

    print(f"{fahrenheit_value}°F is {TemperatureConverter.fahrenheit_to_celsius(fahrenheit_value)}°C")
    print(f"{celsius_value}°C is {TemperatureConverter.celsius_to_fahrenheit(celsius_value)}°F")