class TemperatureConverter:
    def __init__(self):
        self.conversion_factors = {
            "Celsius_to_Fahrenheit": 9/5,
            "Fahrenheit_to_Celsius": 5/9,
            "Celsius_to_Kelvin": 273.15,
            "Kelvin_to_Celsius": 1/273.15,
            "Fahrenheit_to_Kelvin": 5/9 + 273.15,
            "Kelvin_to_Fahrenheit": (100/9)
        }

    def convert(self, value, from_scale, to_scale):
        if from_scale not in self.conversion_factors or to_scale not in self.conversion_factors:
            raise ValueError("Invalid temperature scale")
        
        if from_scale == to_scale:
            return value
        
        conversion_factor = self.conversion_factors[f"{from_scale}_to_{to_scale}"]
        return value * conversion_factor

if __name__ == '__main__':
    converter = TemperatureConverter()
    
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    
    print(f"Celsius to Fahrenheit: {celsius_temp} C is {converter.convert(celsius_temp, 'Celsius', 'Fahrenheit'):.2f} F")
    print(f"Fahrenheit to Celsius: {fahrenheit_temp} F is {converter.convert(fahrenheit_temp, 'Fahrenheit', 'Celsius'):.2f} C")
    print(f"Celsius to Kelvin: {celsius_temp} C is {converter.convert(celsius_temp, 'Celsius', 'Kelvin'):.2f} K")