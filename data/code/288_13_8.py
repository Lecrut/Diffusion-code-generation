def celsius_to_fahrenheit(temperatures):
    if not all(isinstance(temp, (int, float)) and temp >= -273.15 for temp in temperatures):
        raise ValueError("All temperatures must be numbers and greater than or equal to absolute zero.")
    return [(temp * 9/5) + 32 for temp in temperatures]

if __name__ == '__main__':
    temperatures_celsius = [0, -40, 100]
    try:
        temperatures_fahrenheit = celsius_to_fahrenheit(temperatures_celsius)
        print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
    except ValueError as e:
        print(e)