def fahrenheit_to_celsius(fahrenheit: float) -> float:
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    sample_temperatures = [32.0, 68.0, 100.0]
    min_celsius = fahrenheit_to_celsius(min(sample_temperatures))
    print(f"Minimum temperature in Celsius: {min_celsius:.2f}")