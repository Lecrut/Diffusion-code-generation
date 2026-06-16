if __name__ == '__main__':
    temperatures_celsius = [0, 10, 20, 30, 45]
    for celsius in temperatures_celsius:
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit:.2f}, Kelvin: {kelvin:.2f}")