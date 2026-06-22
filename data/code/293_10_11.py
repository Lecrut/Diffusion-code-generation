def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    sample_temperatures = [0, 100, -40, 37]
    for temp in sample_temperatures:
        if isinstance(temp, (int, float)):
            fahrenheit = celsius_to_fahrenheit(temp)
            print(f"{temp}C -> {fahrenheit:.2f}F")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}F -> {celsius:.2f}C")