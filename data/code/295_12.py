def convert_temperature(temperature, unit):
    if unit.lower() == 'c':
        if temperature == 0:
            return 32.0
        else:
            return (temperature * 9/5) + 32
    elif unit.lower() == 'f':
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
    freezing_c = 0.0
    freezing_f = convert_temperature(freezing_c, 'C')
    print(f"{freezing_c}°C is {freezing_f}°F")
    boiling_c = 100.0
    boiling_f = convert_temperature(boiling_c, 'C')
    print(f"{boiling_c}°C is {boiling_f}°F")