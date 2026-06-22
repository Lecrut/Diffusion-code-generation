def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    sample_temperatures = [32, 212, -40, 0, 100]
    min_temp_celsius = fahrenheit_to_celsius(min(sample_temperatures))
    print(f"Minimum temperature in Celsius: {min_temp_celsius:.2f}")