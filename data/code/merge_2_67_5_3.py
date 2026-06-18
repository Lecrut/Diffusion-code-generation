def convert_temperature(value):
    try:
        temp = float(value)
    except ValueError as e:
        return f"Error: Invalid temperature value '{value}'. Please provide a numeric value."
    celsius = temp - 32 * (5 / 9)
    fahrenheit = temp * (9 / 5) + 32
    kelvin = temp + 273.15
    return {
        "Celsius": round(celsius, 2),
        "Fahrenheit": round(fahrenheit, 2),
        "Kelvin": round(kelvin, 2)
    }
if __name__ == '__main__':
    samples = [0, -40, 100]
    for sample in samples:
        result = convert_temperature(sample)
        print(f"Input {sample}:")
        if isinstance(result, str):
            print(result)
        else:
            print(result)