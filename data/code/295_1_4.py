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
    fahrenheit_temp = 77
    c_to_f = convert_temperature(celsius_temp, "C")
    f_to_c = convert_temperature(fahrenheit_temp, "F")
    print(f"{celsius_temp}°C is {c_to_f:.2f}°F")
    print(f"{fahrenheit_temp}°F is {f_to_c:.2f}°C")