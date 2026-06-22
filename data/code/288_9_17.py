def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    sample_temperatures_fahrenheit = [32, 68, 100]
    min_temperature_celsius = min(fahrenheit_to_celsius(temp) for temp in sample_temperatures_fahrenheit)
    print(f"Minimum temperature: {min_temperature_celsius:.2f} C")