conversion_factors = {
    "Celsius_to_Fahrenheit": 9/5,
    "Fahrenheit_to_Celsius": 5/9,
    "Celsius_to_Kelvin": 273.15,
    "Kelvin_to_Celsius": -273.15,
    "Fahrenheit_to_Kelvin": 459.67 / 9 * 5 + 273.15,
    "Kelvin_to_Fahrenheit": 9/5 * 459.67
}

def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    factor = conversion_factors.get(f"{from_scale}_to_{to_scale}")
    if factor is not None:
        return value * factor
    else:
        raise ValueError("Unsupported temperature scale conversion")

if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    
    print(f"Celsius to Fahrenheit: {celsius_temp}°C is {convert_temperature(celsius_temp, 'Celsius', 'Fahrenheit'):.2f}°F")
    print(f"Fahrenheit to Celsius: {fahrenheit_temp}°F is {convert_temperature(fahrenheit_temp, 'Fahrenheit', 'Celsius'):.2f}°C")
    print(f"Celsius to Kelvin: {celsius_temp}°C is {convert_temperature(celsius_temp, 'Celsius', 'Kelvin'):.2f}K")