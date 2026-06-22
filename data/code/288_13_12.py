def celsius_to_fahrenheit(celsius_list):
    if not isinstance(celsius_list, list) or not all(isinstance(temp, (int, float)) for temp in celsius_list):
        raise ValueError("Input must be a list of integers or floats")
    
    fahrenheit_list = [(c * 9/5) + 32 for c in celsius_list]
    return fahrenheit_list

if __name__ == '__main__':
    temperatures_celsius = [0, 10, 20, 30, 40]
    try:
        temperatures_fahrenheit = celsius_to_fahrenheit(temperatures_celsius)
        print(f"Fahrenheit: {temperatures_fahrenheit}")
    except ValueError as e:
        print(e)