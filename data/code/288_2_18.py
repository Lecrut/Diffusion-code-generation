def calculate_average_temperature(celsius_list: list) -> float:
    if not all(isinstance(temp, (int, float)) for temp in celsius_list):
        raise ValueError("All elements in the list must be numbers.")
    
    average_celsius = sum(celsius_list) / len(celsius_list)
    average_fahrenheit = (average_celsius * 9/5) + 32
    return average_fahrenheit

if __name__ == '__main__':
    sample_temperatures = [20.5, 22.3, 19.8, 24.1]
    print(calculate_average_temperature(sample_temperatures))