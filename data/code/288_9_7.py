def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9/5) + 32
    return {
        "celsius": celsius,
        "kelvin": kelvin,
        "fahrenheit": fahrenheit
    }
if __name__ == '__main__':
    sample_celsius = 25.0
    results = convert_temperature(sample_celsius)
    print(f"Celsius: {results['celsius']}")
    print(f"Kelvin: {results['kelvin']}")
    print(f"Fahrenheit: {results['fahrenheit']}")
    sample_celsius_freezing = 0.0
    results_freezing = convert_temperature(sample_celsius_freezing)
    print("\n--- Freezing Point (0°C) ---")
    print(f"Celsius: {results_freezing['celsius']}")
    print(f"Kelvin: {results_freezing['kelvin']}")
    print(f"Fahrenheit: {results_freezing['fahrenheit']}")
    sample_celsius_boiling = 100.0
    results_boiling = convert_temperature(sample_celsius_boiling)
    print("\n--- Boiling Point (100°C) ---")
    print(f"Celsius: {results_boiling['celsius']}")
    print(f"Kelvin: {results_boiling['kelvin']}")
    print(f"Fahrenheit: {results_boiling['fahrenheit']}")