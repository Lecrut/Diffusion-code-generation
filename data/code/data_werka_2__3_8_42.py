def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temperatures = [0, 100, -40, 37, 25]
    fahrenheit_temperatures = [celsius_to_fahrenheit(c) for c in sample_temperatures]
    print(fahrenheit_temperatures)