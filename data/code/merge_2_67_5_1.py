import sys
def convert_temperature(temp: float) -> dict[str, str]:
    try:
        if not isinstance(temp, (int, float)):
            return {"error": "Input must be a number"}
        celsius = temp - 32 * 5 / 9
        fahrenheit = temp * 9 / 5 + 32
        kelvin = temp + 459.67
        if not (celsius == float(celsius) and fahrenheit == float(fahrenheit)):
            return {"error": "Invalid calculation detected"}
        return {
            "Celsius": str(round(celsius, 2)),
            "Fahrenheit": str(round(fahrenheit, 2)),
            "Kelvin": str(round(kelvin, 2))
        }
    except Exception as e:
        return {"error": f"Unexpected error occurred: {str(e)}"}
if __name__ == '__main__':
    sample_temps = [0.0, -459.67, 100.0]
    for temp in sample_temps:
        result = convert_temperature(temp)
        print(f"Input ({temp}) -> {result}")