def convert_temperature(temperature, unit):
    if unit == 'C':
        if temperature == 0:
            return 32.0
        else:
            return (temperature * 9/5) + 32
    elif unit == 'F':
        if temperature == 32:
            return 0.0
        else:
            return (temperature - 32) * 5/9
    else:
        raise ValueError("Invalid unit specified. Use 'C' for Celsius or 'F' for Fahrenheit.")
if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit_result = convert_temperature(celsius_temp, 'C')
    print(f"{celsius_temp}°C is {fahrenheit_result}°F")
    fahrenheit_temp = 77.0
    celsius_result = convert_temperature(fahrenheit_temp, 'F')
    print(f"{fahrenheit_temp}°F is {celsius_result}°C")
    freezing_celsius = 0.0
    freezing_fahrenheit = convert_temperature(freezing_celsius, 'C')
    print(f"{freezing_celsius}°C is {freezing_fahrenheit}°F")
    boiling_celsius = 100.0
    boiling_fahrenheit = convert_temperature(boiling_celsius, 'C')
    print(f"{boiling_celsius}°C is {boiling_fahrenheit}°F")