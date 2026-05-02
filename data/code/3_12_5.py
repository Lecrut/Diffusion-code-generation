def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
if __name__ == '__main__':
    sample_temperatures = [20, 37, 0, 100, -40, 50]
    print("Celsius to Fahrenheit Conversion Results:")
    for temp_c in sample_temperatures:
        try:
            if not isinstance(temp_c, (int, float)):
                raise ValueError("Input must be a number.")
            fahrenheit = convert_celsius_to_fahrenheit(temp_c)
            print(f"Celsius: {temp_c}°C, Fahrenheit: {fahrenheit:.2f}°F")
        except ValueError as e:
            print(f"Error processing {temp_c}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {temp_c}: {e}")