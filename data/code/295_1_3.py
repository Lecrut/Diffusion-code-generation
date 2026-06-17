def convert_temperature(temperature, unit):
    if unit == "C":
        if temperature == 0:
            return 32.0
        else:
            return (temperature * 9/5) + 32
    elif unit == "F":
        return (temperature - 32) * 5/9
    else:
        raise ValueError("Invalid unit specified. Use 'C' or 'F'.")
if __name__ == '__main__':
    celsius_temp = 25
    fahrenheit_temp = convert_temperature(celsius_temp, "C")
    print(f"{celsius_temp}°C is {fahrenheit_temp:.2f}°F")
    fahrenheit_input = 77
    celsius_output = convert_temperature(fahrenheit_input, "F")
    print(f"{fahrenheit_input}°F is {celsius_output:.2f}°C")
    freezing_celsius = 0
    freezing_fahrenheit = convert_temperature(freezing_celsius, "C")
    print(f"{freezing_celsius}°C is {freezing_fahrenheit:.2f}°F")
    boiling_celsius = 100
    boiling_fahrenheit = convert_temperature(boiling_celsius, "C")
    print(f"{boiling_celsius}°C is {boiling_fahrenheit:.2f}°F")