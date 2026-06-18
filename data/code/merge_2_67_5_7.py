def convert_temperature(temp_input):
    try:
        temp_value = float(temp_input)
        if not isinstance(temp_value, (int, float)):
            raise TypeError("Input must be a numeric value.")
        celsius = temp_value - 32 * 5 / 9
        fahrenheit = temp_value * 9 / 5 + 32
        kelvin = temp_value + 459.67
        return {
            "Celsius": round(celsius, 2),
            "Fahrenheit": round(fahrenheit, 2),
            "Kelvin": round(kelvin, 2)
        }
    except ValueError:
        raise ValueError("Invalid input: Please provide a valid number.")
if __name__ == '__main__':
    samples = [0, -40, 100]
    for sample in samples:
        try:
            result = convert_temperature(sample)
            print(f"Input {sample}:")
            print(result)
        except ValueError as e:
            print(f"Error converting temperature {sample}: {e}")