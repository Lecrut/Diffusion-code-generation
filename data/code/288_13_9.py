def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(temperatures_celsius):
    return [celsius_to_fahrenheit(temp) for temp in temperatures_celsius]

if __name__ == '__main__':
    sample_temperatures = [0, 10, 20, 30, 40]
    converted_temperatures = convert_temperatures(sample_temperatures)
    print(converted_temperatures)