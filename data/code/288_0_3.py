import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    print(f"Celsius: {celsius_temp}")
    print(f"Fahrenheit: {fahrenheit_temp}")
    print(f"Kelvin: {kelvin_temp}")
    c_to_f = celsius_to_fahrenheit(celsius_temp)
    f_to_c = fahrenheit_to_celsius(fahrenheit_temp)
    c_to_k = celsius_to_kelvin(celsius_temp)
    k_to_c = kelvin_to_celsius(kelvin_temp)
    f_to_k = fahrenheit_to_kelvin(fahrenheit_temp)
    k_to_f = kelvin_to_fahrenheit(kelvin_temp)
    print("\n--- Conversions ---")
    print(f"{celsius_temp}°C is equal to {c_to_f:.2f}°F")
    print(f"{fahrenheit_temp}°F is equal to {f_to_c:.2f}°C")
    print(f"{celsius_temp}°C is equal to {c_to_k:.2f}K")
    print(f"{kelvin_temp}K is equal to {k_to_f:.2f}°F")