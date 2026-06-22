def celsius_to_fahrenheit(celsius_list):
    if not all(isinstance(temp, (int, float)) for temp in celsius_list):
        raise ValueError("All temperatures must be integers or floats.")
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [30, -10, 100, 45]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)