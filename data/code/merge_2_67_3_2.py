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
        temp_in_fahrenheit = converter.to_fahrenheit(value)
        temp_in_kelvin = converter.to_kelvin(value)
        return {
            'Fahrenheit': round(temp_in_fahrenheit, 2),
            'Kelvin': round(temp_in_kelvin, 2)
        } if to_scale in ['F', 'K'] else None
    elif from_scale == 'F':
        temp_in_celsius = converter.to_celsius(value)
        return {
            'Celsius': round(temp_in_celsius, 2),
            'Kelvin': round(converter.to_kelvin(temp_in_celsius), 2)
        } if to_scale in ['C', 'K'] else None
    elif from_scale == 'K':
        temp_in_celsius = converter.to_celsius_from_kelvin(value)
        return {
            'Celsius': round(temp_in_celsius, 2),
            'Fahrenheit': round(converter.to_fahrenheit(temp_in_celsius), 2)
        } if to_scale in ['C', 'F'] else None
    elif from_scale == 'R' or from_scale == 'Reaumur':
        temp_in_kelvin = value * (5 / 4) + 273.15
        return {
            'Kelvin': round(temp_in_kelvin, 2),
            'Celsius': round(temp_in_kelvin - 273.15, 2),
            'Fahrenheit': round((temp_in_celsius * 9 / 5) + 32, 2) if to_scale == 'F' else None,
            'Reaumur': round(value * (4/5), 2) if to_scale in ['R', 'Reaumur'] else None
        }
if __name__ == '__main__':
    test_cases = [
        {'value': 0, 'from_scale': 'C'},
        {'value': 32, 'from_scale': 'F'},
        {'value': 273.15, 'from_scale': 'K'}
    ]
    for case in test_cases:
        result = convert_temperature(case['value'], case['from_scale'], 'C')
        print(f"{case['value']} {case['from_scale'].upper()} -> Celsius: {result}")