def max_temperature_in_fahrenheit(temperatures_celsius):
    if not temperatures_celsius:
        return None
    max_celsius = max(temperatures_celsius)
    return (max_celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [10, -5, 20, 30]
    print(max_temperature_in_fahrenheit(sample_temps))