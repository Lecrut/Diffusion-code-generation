def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
if __name__ == '__main__':
    sample_temperatures = [20, 37, 0, 100, -40, 50]
    for temp_c in sample_temperatures:
        try:
            temp_c = float(temp_c)
            temp_f = convert_celsius_to_fahrenheit(temp_c)
            print(f"Celsius: {temp_c:.2f}°C, Fahrenheit: {temp_f:.2f}°F")
        except ValueError:
            print(f"Invalid input encountered: {temp_c}. Skipping this reading.")