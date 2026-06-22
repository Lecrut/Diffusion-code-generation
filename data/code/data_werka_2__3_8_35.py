def celsius_to_fahrenheit(celsius_list):
    if not all(isinstance(c, (int, float)) for c in celsius_list):
        raise ValueError("All elements in the list must be numbers.")
    return [(c * 9/5) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, -10, 0, 15.5, 100]
    try:
        fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
        print(fahrenheit_temperatures)
    except ValueError as e:
        print(e)