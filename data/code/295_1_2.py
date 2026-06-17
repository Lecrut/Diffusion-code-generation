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
    temp_c = 25
    temp_f = convert_temperature(temp_c, 'C')
    print(f"{temp_c}°C is {temp_f:.2f}°F")
    temp_f_to_c = 68
    temp_c_from_f = convert_temperature(temp_f_to_c, 'F')
    print(f"{temp_f_to_c}°F is {temp_c_from_f:.2f}°C")
    temp_freezing = 0
    temp_freezing_f = convert_temperature(temp_freezing, 'C')
    print(f"{temp_freezing}°C is {temp_freezing_f:.2f}°F")
    temp_boiling = 100
    temp_boiling_f = convert_temperature(temp_boiling, 'C')
    print(f"{temp_boiling}°C is {temp_boiling_f:.2f}°F")