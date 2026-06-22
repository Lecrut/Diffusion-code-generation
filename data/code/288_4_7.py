TEMPERATURE_CONVERSION = {
    "C": 9/5,
    "F": 32
}

def celsius_to_fahrenheit(celsius):
    return (celsius * TEMPERATURE_CONVERSION["C"]) + TEMPERATURE_CONVERSION["F"]

if __name__ == '__main__':
    sample_temps = [0, 10, 20, 25, 30]
    fahrenheit_temps = [celsius_to_fahrenheit(temp) for temp in sample_temps]
    print(fahrenheit_temps)