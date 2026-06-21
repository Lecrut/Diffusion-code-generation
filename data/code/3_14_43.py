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

    def convert_to_celsius(self):
        return self.kelvin - 273.15

    def convert_to_fahrenheit(self):
        celsius = self.convert_to_celsius()
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        converter = TemperatureConverter(kelvin)
        fahrenheit = converter.convert_to_fahrenheit()
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")