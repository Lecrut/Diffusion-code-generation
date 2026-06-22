conversion_factors = {
    'Celsius': {'Fahrenheit': 9/5, 'Kelvin': 1},
    'Fahrenheit': {'Celsius': 5/9, 'Kelvin': 5/9},
    'Kelvin': {'Celsius': -273.15, 'Fahrenheit': (5/9) * 9}
}

def convert_temperature(temperature, from_unit, to_unit):
    if from_unit == to_unit:
        return temperature
    factor = conversion_factors[from_unit][to_unit]
    return temperature * factor + conversion_factors[from_unit]['Kelvin']

if __name__ == '__main__':
    sample_fahrenheit = 77.0
    result_celsius = convert_temperature(sample_fahrenheit, 'Fahrenheit', 'Celsius')
    print(f"77.0 F is {result_celsius:.2f} C")