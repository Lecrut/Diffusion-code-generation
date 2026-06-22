def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

class TemperatureConverter:
    def __init__(self, kelvin):
        if kelvin < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        self.kelvin = kelvin
        self.celsius = self.convert_to_celsius()
        self.fahrenheit = self.convert_to_fahrenheit()

    def convert_to_celsius(self):
        return kelvin_to_celsius(self.kelvin)

    def convert_to_fahrenheit(self):
        return celsius_to_fahrenheit(self.celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        converter = TemperatureConverter(kelvin)
        print(f"Kelvin: {kelvin} -> Celsius: {converter.celsius}, Fahrenheit: {converter.fahrenheit}")