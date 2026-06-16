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
    temp_c = 25
    temp_f = 77.0
    print(f"{temp_c}°C is {convert_temperature(temp_c, 'C'):.2f}°F")
    print(f"{temp_f}°F is {convert_temperature(temp_f, 'F'):.2f}°C")
    print(f"0°C is {convert_temperature(0, 'C'):.2f}°F")
    print(f"{32}°F is {convert_temperature(32, 'F'):.2f}°C")
    try:
        convert_temperature(10, 'K')
    except ValueError as e:
        print(f"Error caught: {e}")