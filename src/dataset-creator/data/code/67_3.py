class TemperatureConverter:
    def to_celsius(self, temperature):
        return (temperature - 32) * 5 / 9
    def to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, celsius):
        return celsius + 273.15
    def to_celsius_from_kelvin(self, kelvin):
        return kelvin - 273.15
def convert_temperature(value, from_scale, to_scale):
    converter = TemperatureConverter()
    if from_scale == 'C':
        temp_value = value
    elif from_scale == 'F':
        temp_value = (value * 9 / 5) + 32
    else:    
        temp_value = value - 273.15
    celsius_temp = converter.to_celsius(temp_value)
    if to_scale == 'C':
        return round(celsius_temp, 4)
    elif to_scale == 'F':
        return round(converter.to_fahrenheit(celsius_temp), 4)
    else:    
        return round(converter.to_kelvin(celsius_temp), 4)
if __name__ == '__main__':
    test_cases = [
        ('C', 25, 'F'),
        ('F', 77, 'K'),
        ('K', 300, 'C'),
        ('C', -10, 'F'),
        ('F', 98.6, 'C')
    ]
    for from_s, val, to_s in test_cases:
        result = convert_temperature(val, from_s, to_s)
        print(f"{val} {from_s} is equal to {result} {to_s}")