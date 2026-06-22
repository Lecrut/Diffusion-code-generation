def calculate_average_temperature(celsius_list):
    if not celsius_list:
        return None
    average_celsius = sum(celsius_list) / len(celsius_list)
    average_fahrenheit = (average_celsius * 9/5) + 32
    return average_fahrenheit

if __name__ == '__main__':
    sample_temperatures = [10, 20, 30, 40, 50]
    print(calculate_average_temperature(sample_temperatures))