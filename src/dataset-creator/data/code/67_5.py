def convert_temperature(temp_value):
    try:
        temp = float(temp_value)
    except ValueError as e:
        return f"Error: Invalid temperature value '{temp_value}'. Expected a number."
    celsius = temp - 32 * (5 / 9)
    fahrenheit = temp * (9 / 5) + 32
    kelvin = temp + 273.15
    return {
        "Celsius": round(celsius, 2),
        "Fahrenheit": round(fahrenheit, 2),
        "Kelvin": round(kelvin, 2)
    }
if __name__ == '__main__':
    sample_temps = [0, -40, 100]
    for t in sample_temps:
        result = convert_temperature(t)
        print(f"Input {t} -> {result}")