def convert_temperature(temp):
    try:
        temp = float(temp)
        celsius = temp - 32 * (5 / 9)
        fahrenheit = temp * (9 / 5) + 32
        kelvin = temp + 273.15
        return {
            "Celsius": round(celsius, 2),
            "Fahrenheit": round(fahrenheit, 2),
            "Kelvin": round(kelvin, 2)
        }
    except ValueError:
        raise TypeError("Input must be a numeric value representing temperature.")
if __name__ == '__main__':
    sample_temps = [0, 100, -40]
    for t in sample_temps:
        try:
            result = convert_temperature(t)
            print(f"Temperature {t} converted to:\n{result}")
        except TypeError as e:
            print(f"Error converting temperature {t}: {e}")