def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    temp_celsius = 0.0
    try:
        temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
        print(f"{temp_celsius}°C is {temp_fahrenheit}°F")
    except TypeError as e:
        print(f"Error: {e}")

    temp_celsius_error = "100"
    try:
        temp_fahrenheit_error = celsius_to_fahrenheit(temp_celsius_error)
        print(f"{temp_celsius_error}°C is {temp_fahrenheit_error}°F")
    except TypeError as e:
        print(f"Error: {e}")