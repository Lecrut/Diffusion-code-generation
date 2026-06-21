class TemperatureConverter:
    KELVIN_OFFSET = 273.15

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def kelvin_to_celsius(kelvin):
        if kelvin < TemperatureConverter.KELVIN_OFFSET:
            raise ValueError("Kelvin temperature cannot be below absolute zero")
        return kelvin - TemperatureConverter.KELVIN_OFFSET

if __name__ == '__main__':
    sample_celsius = 50
    sample_fahrenheit = 122
    sample_kelvin = 323.15
    converter = TemperatureConverter()
    
    print(f"{sample_celsius}C is {converter.celsius_to_fahrenheit(sample_celsius)}F")
    print(f"{sample_fahrenheit}F is {converter.fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"{sample_kelvin}K is {converter.kelvin_to_celsius(sample_kelvin)}C")