def find_max_temperature(celsius_list):
    max_celsius = max(celsius_list)
    return (max_celsius * 9/5) + 32

if __name__ == '__main__':
    temperatures_celsius = [0, 100, -40, 25]
    max_temp_fahrenheit = find_max_temperature(temperatures_celsius)
    print(f"Maximum temperature: {max_temp_fahrenheit}°F")