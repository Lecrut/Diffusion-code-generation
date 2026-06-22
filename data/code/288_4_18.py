TEMPERATURE_CONVERSION_FACTOR = 9/5
ADDITIONAL_OFFSET = 32

def celsius_to_fahrenheit(celsius):
    return (celsius * TEMPERATURE_CONVERSION_FACTOR) + ADDITIONAL_OFFSET

if __name__ == '__main__':
    sample_temps = [0, 10, 20, 25, 30]
    fahrenheit_temps = [celsius_to_fahrenheit(temp) for temp in sample_temps]
    print(fahrenheit_temps)