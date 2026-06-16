def convert_temperature(temperature, unit):
    if unit.lower() == 'c':
        if temperature > -273.15:
            fahrenheit = (temperature * 9/5) + 32
            return fahrenheit
        else:
            return "Error: Temperature below absolute zero"
    elif unit.lower() == 'f':
        if temperature > -459.67:
            celsius = (temperature - 32) * 5/9
            return celsius
        else:
            return "Error: Temperature below absolute zero"
    else:
        return "Error: Invalid unit. Use 'C' or 'F'"
if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit_result = convert_temperature(celsius_temp, 'C')
    print(f"{celsius_temp}°C is {fahrenheit_result}°F")
    fahrenheit_temp = 77.0
    celsius_result = convert_temperature(fahrenheit_temp, 'F')
    print(f"{fahrenheit_temp}°F is {celsius_result}°C")
    freezing_point_c = 0.0
    freezing_point_f = convert_temperature(freezing_point_c, 'C')
    print(f"{freezing_point_c}°C is {freezing_point_f}°F")
    boiling_point_c = 100.0
    boiling_point_f = convert_temperature(boiling_point_c, 'C')
    print(f"{boiling_point_c}°C is {boiling_point_f}°F")