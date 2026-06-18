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
        raise TypeError("Input must be a number representing temperature.")
if __name__ == '__main__':
    sample_temps = [0, 15.6, -40]
    for temp in sample_temps:
        print(f"Converting {temp} to all scales:")
        result = convert_temperature(temp)
        if "Error" in str(result):
            print(result["Message"])
        else:
            print(f"Celsius: {result['Celsius']}")
            print(f"Fahrenheit: {result['Fahrenheit']}")
            print(f"Kelvin: {result['Kelvin']}")