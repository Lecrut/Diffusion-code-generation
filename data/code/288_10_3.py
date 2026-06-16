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
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    sample_kelvin = 298.15
    print("--- Temperature Conversion Demonstration ---")
    print("\nSample Celsius to other scales:")
    c_to_f = celsius_to_fahrenheit(sample_celsius)
    c_to_k = celsius_to_kelvin(sample_celsius)
    print(f"{sample_celsius}°C is {c_to_f:.2f}°F")
    print(f"{sample_celsius}°C is {c_to_k:.2f}K")
    print("\nSample Fahrenheit to other scales:")
    f_to_c = fahrenheit_to_celsius(sample_fahrenheit)
    f_to_k = fahrenheit_to_kelvin(sample_fahrenheit)
    print(f"{sample_fahrenheit}°F is {f_to_c:.2f}°C")
    print(f"{sample_fahrenheit}°F is {f_to_k:.2f}K")
    print("\nSample Kelvin to other scales:")
    k_to_c = kelvin_to_celsius(sample_kelvin)
    k_to_f = kelvin_to_fahrenheit(sample_kelvin)
    print(f"{sample_kelvin}K is {k_to_c:.2f}°C")
    print(f"{sample_kelvin}K is {k_to_f:.2f}°F")