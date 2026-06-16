def convert_temperature(temperature, unit):
    if unit == "to_c":
        if temperature == 0:
            return 0.0
        else:
            return (temperature - 32) * 5 / 9
    elif unit == "to_f":
        return (temperature * 9 / 5) + 32
    else:
        raise ValueError("Invalid unit specified. Use 'to_c' or 'to_f'.")
if __name__ == '__main__':
    temp_c = 25
    temp_f = 77
    result_f = convert_temperature(temp_c, "to_f")
    result_c = convert_temperature(temp_f, "to_c")
    print(f"25 Celsius is {result_f:.2f} Fahrenheit")
    print(f"77 Fahrenheit is {result_c:.2f} Celsius")