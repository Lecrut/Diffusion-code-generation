import math
def convert_temperature(temperature, unit):
    if unit == 'C':
        if temperature == 0:
            return 32.0
        else:
            return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    else:
        raise ValueError("Invalid unit specified. Use 'C' or 'F'.")
if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit = convert_temperature(celsius_temp, 'F')
    print(f"{celsius_temp}°C is {fahrenheit:.2f}°F")
    fahrenheit_temp = 77.0
    celsius = convert_temperature(fahrenheit_temp, 'C')
    print(f"{fahrenheit_temp}°F is {celsius:.2f}°C")
    freezing_c = 0.0
    freezing_f = convert_temperature(freezing_c, 'F')
    print(f"{freezing_c}°C is {freezing_f:.2f}°F")
    boiling_c = 100.0
    boiling_f = convert_temperature(boiling_c, 'F')
    print(f"{boiling_c}°C is {boiling_f:.2f}°F")