def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
if __name__ == '__main__':
    c_sample = 25.0
    f_sample = 77.0
    k_sample = 300.0
    f_from_c = celsius_to_fahrenheit(c_sample)
    c_from_f = fahrenheit_to_celsius(f_sample)
    c_from_k = kelvin_to_celsius(k_sample)
    print(f"Celsius to Fahrenheit: {c_sample}°C is {f_from_c:.2f}°F")
    print(f"Fahrenheit to Celsius: {f_sample}°F is {c_from_f:.2f}°C")
    print(f"Kelvin to Celsius: {k_sample}K is {c_from_k:.2f}°C")