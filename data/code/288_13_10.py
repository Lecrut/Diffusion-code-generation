def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number")
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    temperatures_celsius = [0, 10, 20, 30, 40]
    temperatures_fahrenheit = [celsius_to_fahrenheit(temp) for temp in temperatures_celsius]
    print(temperatures_fahrenheit)