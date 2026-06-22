def find_max_temperature_celsius(temperatures):
    max_celsius = max(temperatures)
    return (max_celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temperatures = [15, 22, -3, 0, 45]
    print(find_max_temperature_celsius(sample_temperatures))