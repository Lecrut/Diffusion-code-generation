import math
def create_temperature_converter():
    conversion_factors = {
        "Celsius_to_Fahrenheit": 1.8,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 1/273.15,
        "Fahrenheit_to_Kelvin": 5/9 + 273.15,
        "Kelvin_to_Fahrenheit": (1/273.15) * 9/5 - 459.67
    }
    return conversion_factors
if __name__ == '__main__':
    converters = create_temperature_converter()
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    print(f"Celsius to Fahrenheit: {celsius_temp}°C is {celsius_temp * converters['Celsius_to_Fahrenheit']:.2f}°F")
    print(f"Fahrenheit to Celsius: {fahrenheit_temp}°F is {fahrenheit_temp * converters['Fahrenheit_to_Celsius']:.2f}°C")
    print(f"Celsius to Kelvin: {celsius_temp}°C is {celsius_temp * converters['Celsius_to_Kelvin']:.2f}K")
    print(f"Kelvin to Celsius: {kelvin_temp}K is {kelvin_temp * converters['Kelvin_to_Celsius']:.2f}°C")
    print(f"Fahrenheit to Kelvin: {fahrenheit_temp}°F is {fahrenheit_temp * converters['Fahrenheit_to_Kelvin']:.2f}K")
    print(f"Kelvin to Fahrenheit: {kelvin_temp}K is {kelvin_temp * converters['Kelvin_to_Fahrenheit']:.2f}°F")