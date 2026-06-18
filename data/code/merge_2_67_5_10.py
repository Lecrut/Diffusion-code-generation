def convert_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError("Input must be a number.")
    celsius = temp - 32 * 5 / 9
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    return {
        "Celsius": round(celsius, 2),
        "Fahrenheit": round(fahrenheit, 2),
        "Kelvin": round(kelvin, 2)
    }
if __name__ == '__main__':
    sample_temps = [0, -40, 100]
    for temp in sample_temps:
        try:
            result = convert_temperature(temp)
            print(f"Input {temp}°C -> Fahrenheit: {result['Fahrenheit']}°, Kelvin: {result['Kelvin']}K")
        except Exception as e:
            print(f"Error converting temperature for input {temp}: {e}")