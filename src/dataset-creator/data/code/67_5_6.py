def convert_temperature(temp_input):
    try:
        temp = float(temp_input)
    except ValueError as e:
        return f"Error: Invalid temperature value '{temp_input}'. Please provide a numeric input."
    celsius = temp - 32 * (5 / 9)
    fahrenheit = temp * (9 / 5) + 32
    kelvin = temp + 273.15
    return {
        "Celsius": round(celsius, 2),
        "Fahrenheit": round(fahrenheit, 2),
        "Kelvin": round(kelvin, 2)
    }
if __name__ == '__main__':
    sample_temps = ["10", "-45.6", "37"]
    for temp_str in sample_temps:
        result = convert_temperature(temp_str)
        print(f"Input: {temp_str}")
        if isinstance(result, dict):
            print("Converted Values:", result)
        else:
            print(result)