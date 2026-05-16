def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
if __name__ == '__main__':
    c_val = 25.0
    f_val = 77.0
    k_val = 300.0
    c_to_f = celsius_to_fahrenheit(c_val)
    f_to_c = fahrenheit_to_celsius(f_val)
    k_to_c = kelvin_to_celsius(k_val)
    print(f"Celsius to Fahrenheit: {c_val}°C is {c_to_f:.2f}°F")
    print(f"Fahrenheit to Celsius: {f_val}°F is {f_to_c:.2f}°C")
    print(f"Kelvin to Celsius: {k_val}K is {k_to_c:.2f}°C")