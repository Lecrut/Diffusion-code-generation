class TemperatureConverter:
    def to_celsius(self, temperature):
        return (temperature - 32) * 5 / 9
    def to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32
    def to_kelvin(self, celsius):
        return celsius + 273.15
    def from_celcius(self, kelvin):
        return kelvin - 273.15
    def from_fahrenheit(self, celsius):
        return (celsius - 32) * 9 / 5
def convert_temperature(value, source_scale, target_scale):
    converters = {
        'C': TemperatureConverter(),
        'F': lambda t: t * 1.8 + 32,
        'K': lambda t: t + 273.15
    }
    reverse_converters = {
        'C': lambda c: (c - 32) / 1.8,
        'F': lambda f: (f - 32) * 0.5556,
        'K': lambda k: k - 273.15
    }
    if source_scale == target_scale:
        return value
    intermediate = TemperatureConverter()
    if source_scale in ['C', 'F'] and target_scale == 'C':
        return intermediate.to_celsius(value) if source_scale == 'C' else intermediate.from_fahrenheit(value)
    elif source_scale in ['C', 'K'] and target_scale == 'C':
        return value - 273.15 if source_scale == 'K' else value * (9/5) + 32                                           
    temp = TemperatureConverter()
    celsius_val = None
    if source_scale == 'C':
        celsius_val = value
    elif source_scale == 'F':
        celsius_val = (value - 32) * 5 / 9
    else:         
        celsius_val = value - 273.15
    if target_scale == 'C':
        return round(celsius_val, 4)
    elif target_scale == 'F':
        result_cel_to_f = temp.to_fahrenheit(celsius_val)
        return round(result_cel_to_f, 4)
    else:         
        result_kelvin = celsius_val + 273.15
        return round(result_kelvin, 4)
if __name__ == '__main__':
    test_cases = [
        (0, 'C', 'F'),
        (100, 'F', 'K'),
        (-40, 'C', 'F'),
        (32, 'F', 'C'),
        (273.15, 'K', 'C')
    ]
    for val, src, dst in test_cases:
        result = convert_temperature(val, src, dst)
        print(f"{val} {src.upper()} is equal to {result:.4f} {dst}")