if __name__ == '__main__':
    temperatures_celsius = [0.0, 10.0, 25.0, 37.0, 100.0]
    for celsius in temperatures_celsius:
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f"Celsius: {celsius:.2f}, Fahrenheit: {fahrenheit:.2f}, Kelvin: {kelvin:.2f}")